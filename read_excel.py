import pandas as pd
import time
import os
from datetime import datetime

# Local files to track processed and crash invoice numbers
LOCAL_RECORD_FILE = "processed_invoices.txt"
CRASH_ENTRIES_FILE = "crash_entries.txt"


def read_excel_file(excel_file):
    """Read the Excel file into a DataFrame, ensuring it exists."""
    if not os.path.exists(excel_file):
        print(f"❌ Error: The file {excel_file} does not exist.")
        return None
    return pd.read_excel(excel_file, engine="openpyxl")


def clean_invoice_data(df):
    """Clean the DataFrame: remove empty, mostly empty rows, and duplicates."""
    if 'InvoiceNo' not in df.columns:
        print("❌ Error: 'InvoiceNo' column not found in the Excel file.")
        return None, None

    df_cleaned = df.dropna(how='all')
    threshold = len(df_cleaned.columns) // 2
    crash_entries = df_cleaned[df_cleaned.count(axis=1) <= threshold]
    df_cleaned = df_cleaned[df_cleaned.count(axis=1) > threshold]
    df_cleaned = df_cleaned[~df_cleaned.apply(lambda row: all(str(cell).strip() in ["", ","] for cell in row), axis=1)]
    df_cleaned = df_cleaned.drop_duplicates(subset='InvoiceNo', keep='first')
    
    return df_cleaned, crash_entries


def load_invoice_ids(file_path):
    """Load invoice IDs from a given file to avoid duplicates."""
    if not os.path.exists(file_path):
        return set()
    with open(file_path, 'r', encoding='utf-8') as f:
        return set(line.strip() for line in f if line.strip().isdigit())


def save_invoice_ids(file_path, invoice_ids, label):
    """Append only the latest batch of invoice numbers with a clear format."""
    if not invoice_ids:
        return
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    batch_header = f"\n-. = {label} Batch - {timestamp} (Total: {len(invoice_ids)}) = .-\n"
    batch_content = "\n".join(sorted(invoice_ids))
    formatted_content = f"{batch_header}\n\n{batch_content}\n\n"
    
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(formatted_content)


def process_and_convert_excel(excel_file, csv_file):
    """Read, clean, and convert Excel to CSV, ensuring only new invoices are added."""
    df = read_excel_file(excel_file)
    if df is None:
        return

    df_cleaned, crash_entries = clean_invoice_data(df)
    if df_cleaned is None:
        return

    processed_invoice_ids = load_invoice_ids(LOCAL_RECORD_FILE)
    new_invoices = df_cleaned[~df_cleaned['InvoiceNo'].astype(str).isin(processed_invoice_ids)]
    
    if new_invoices.empty:
        print("✅ No new invoices to process.")
        return
    
    new_invoices.to_csv(csv_file, mode='w', index=False, header=True)
    print(f"✅ {len(new_invoices)} new invoices saved to CSV.")
    
    save_invoice_ids(LOCAL_RECORD_FILE, new_invoices['InvoiceNo'].astype(str).tolist(), "Processed Invoices")
    save_invoice_ids(CRASH_ENTRIES_FILE, crash_entries['InvoiceNo'].astype(str).tolist(), "Crash Entries")


def read_csv_fast(csv_file):
    """Read CSV efficiently and measure the time."""
    if not os.path.exists(csv_file):
        print(f"❌ Error: The file {csv_file} does not exist.")
        return None
    
    start_time = time.time()
    df = pd.read_csv(csv_file)
    end_time = time.time()
    print(f"✅ CSV reading completed in {end_time - start_time:.2f} seconds")
    return df


if __name__ == "__main__":
    EXCEL_FILE = "customer.xlsx"
    CSV_FILE = "customer.csv"
    
    process_and_convert_excel(EXCEL_FILE, CSV_FILE)
    df = read_csv_fast(CSV_FILE)
