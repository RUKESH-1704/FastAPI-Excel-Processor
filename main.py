from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import pandas as pd
import os

app = FastAPI(title="FastAPI Excel Processor", docs_url="/", openapi_url="/openapi.json")

# Load Excel File Once
EXCEL_FILE = "Data/capbudg.xls"

if not os.path.exists(EXCEL_FILE):
    raise FileNotFoundError(f"{EXCEL_FILE} not found.")

xls = pd.ExcelFile(EXCEL_FILE)
sheet_data = {sheet: xls.parse(sheet) for sheet in xls.sheet_names}

# Enable CORS for local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/list_tables")
def list_tables():
    return {"tables": list(sheet_data.keys())}


@app.get("/get_table_details")
def get_table_details(table_name: str = Query(..., description="Name of the table")):
    if table_name not in sheet_data:
        raise HTTPException(status_code=404, detail="Table not found.")
    
    df = sheet_data[table_name]
    if df.empty or df.shape[1] < 1:
        raise HTTPException(status_code=400, detail="Table is empty or missing first column.")
    
    first_col = df.iloc[:, 0].dropna().astype(str).tolist()
    return {"table_name": table_name, "row_names": first_col}


@app.get("/row_sum")
def row_sum(
    table_name: str = Query(..., description="Name of the table"),
    row_name: str = Query(..., description="Row label from first column"),
):
    if table_name not in sheet_data:
        raise HTTPException(status_code=404, detail="Table not found.")

    df = sheet_data[table_name]

    # Find the row index matching the row_name
    row_index = df[df.iloc[:, 0].astype(str).str.strip() == row_name.strip()].index
    if row_index.empty:
        raise HTTPException(status_code=404, detail="Row name not found in the table.")
    
    row_values = df.iloc[row_index[0], 1:]  # Skip the first column
    numeric_sum = pd.to_numeric(row_values, errors='coerce').sum()

    return {
        "table_name": table_name,
        "row_name": row_name,
        "sum": numeric_sum
    }
