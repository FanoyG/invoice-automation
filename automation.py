import gspread
import csv
import os
import logging

# Set up logging
logging.basicConfig(filename='process.log', level=logging.INFO)

# Google Sheets Credentials & Sheet Name
JSON_KEYFILE = os.getenv('GOOGLE_SHEET_KEYFILE', 'service_account.json')  # Update with actual JSON keyfile path
SHEET_NAME = "Data-automte-ex-sheet"  # Update with actual sheet name
CSV_FILE = "customer.csv"  # CSV file path
LOCAL_RECORD_FILE = "uploaded_invoices.txt"  # Local file to track uploaded invoices

# 🔄 Connect to Google Sheets
def connect_google_sheets():
    try:
        print("🔄 Connecting to Google Sheets...")
        client = gspread.service_account(filename=JSON_KEYFILE)
        sheet = client.open(SHEET_NAME).sheet1  # Access first sheet
        print("✅ Successfully connected!")
        return sheet
    except Exception as e:
        logging.error(f"❌ Google Sheets connection failed: {e}")
        print(f"❌ Google Sheets connection failed: {e}")
        return None

# 🔍 Get Existing Invoice IDs (Avoid Duplicates)
def get_existing_invoice_ids(sheet):
    try:
        data = sheet.get_all_values()
        return set(row[0] for row in data[1:] if row) if data else set()
    except Exception as e:
        logging.error(f"❌ Error fetching existing data: {e}")
        return set()

# 🔄 Upload CSV Data
def upload_csv_to_google_sheets(sheet):
    if sheet is None:
        print("❌ Upload failed: No Google Sheets connection.")
        return

    try:
        print("🔄 Uploading CSV...")

        # ✅ Read CSV File
        if not os.path.exists(CSV_FILE):
            print(f"❌ Error: {CSV_FILE} not found.")
            return

        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            reader = list(csv.reader(f))
        
        if not reader:
            print("❌ CSV is empty.")
            return

        header, rows = reader[0], reader[1:]

        # ✅ Ensure Header is in Google Sheet
        existing_data = sheet.get_all_values()
        if not existing_data or existing_data[0] != header:
            sheet.clear()
            sheet.append_row(header)

        # ✅ Fetch Existing Invoice IDs
        existing_ids = get_existing_invoice_ids(sheet)
        new_rows = [row for row in rows if row and row[0] not in existing_ids]

        if new_rows:
            sheet.append_rows(new_rows)
            print(f"✅ {len(new_rows)} new records added!")
        else:
            print("✅ No new records to add.")

    except Exception as e:
        logging.error(f"❌ Error uploading data: {e}")
        print(f"❌ Error uploading data: {e}")

# ✅ Run Script
if __name__ == "__main__":
    sheet = connect_google_sheets()
    upload_csv_to_google_sheets(sheet)
