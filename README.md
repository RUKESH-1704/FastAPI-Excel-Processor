📊 FastAPI Excel Processor
This is a simple FastAPI-based web service to interact with and process data from an Excel file (capbudg.xls). The API allows you to:

📋 List all sheet names (tables) in the Excel file.

🔍 View available row labels from a selected sheet.

➕ Compute the sum of numeric values in a selected row.


🚀 How to Run
✅ Requirements
Python 3.8+
pip

🧪 Install Dependencies
pip install fastapi uvicorn pandas openpyxl xlrd


▶️ Start the Server

uvicorn main:app --reload
🌐 Access the API
Visit: http://localhost:8000

This will open the Swagger UI to explore and test the endpoints.

📘 API Endpoints
1. GET /list_tables
Description: Lists all sheet names (tables) in the Excel file.

Response:
{
  "tables": [
    "CapBudgWS"
  ]
}

2. GET /get_table_details?table_name=Sheet1
Query Params:

table_name (string) — Name of the sheet.

Description: Returns the row names (i.e., values from the first column) of the given table.

Response:

json
{
  "table_name": "CapBudgWS",
  "row_names": [
    "INITIAL INVESTMENT",
    "Initial Investment=",
    "Opportunity cost (if any)=",
    "Lifetime of the investment",
    "Salvage Value at end of project=",
    "Deprec. method(1:St.line;2:DDB)=",
    "Tax Credit (if any )=",
    "Other invest.(non-depreciable)=",
    "WORKING CAPITAL",
    "Initial Investment in Work. Cap=",
    "Working Capital as % of Rev=",
    "Salvageable fraction at end=",
    "GROWTH RATES",
    "Revenues",
    "Fixed Expenses",
    "Default: The fixed expense growth rate is set equal to the growth rate in revenues by default.",
    "INITIAL INVESTMENT",
    "Investment",
    " - Tax Credit",
    "Net Investment",
    " + Working Cap",
    " + Opp. Cost",
    " + Other invest.",
    "Initial Investment",
    "SALVAGE VALUE",
    "Equipment",
    "Working Capital",
    "OPERATING CASHFLOWS",
    "Lifetime Index",
    "Revenues",
    " -Var. Expenses",
    " - Fixed Expenses",
    "EBITDA",
    " - Depreciation",
    "EBIT",
    " -Tax",
    "EBIT(1-t)",
    " + Depreciation",
    " - ∂ Work. Cap",
    "NATCF",
    "Discount Factor",
    "Discounted CF",
    "Book Value (beginning)",
    "Depreciation",
    "BV(ending)"
  ]
}

3. GET /row_sum?table_name=Sheet1&row_name=2011-2012
Query Params:

table_name (string) — Name of the sheet.

row_name (string) — Value from the first column of the sheet.

Description: Computes the sum of all numeric values in the specified row (excluding the first column).

Response:

json

{
  "table_name": "CapBudgWS",
  "row_name": "Revenues",
  "sum": 0.4
}

🛡️ Error Handling
404: If the sheet or row name is not found.

400: If the table is empty or invalid format.

🔄 CORS Support
CORS is enabled for all origins for easy local and frontend integration.

📌 Notes
This app loads the Excel file once at startup for performance.

Only .xls and .xlsx files compatible with pandas are supported.

Make sure capbudg.xls is placed in the Data/ directory.


📈 Potential Improvements
Support for .xlsx, .csv, or even Google Sheets integration.

Add filtering, aggregation, and advanced analytics options.

Provide a simple front-end interface using React or Streamlit.

Implement row and column data preview.


⚠️ Missed Edge Cases
Excel file is missing or corrupt.

Tables with merged cells or inconsistent formatting.

Rows with no numeric content (sum will be 0).

Empty first column or non-unique row names.

Unicode or special character issues in headers.