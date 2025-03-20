# 📊 **Invoice Data Entry Automation with Python**

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python) ![Google Sheets API](https://img.shields.io/badge/Google_Sheets_API-Enabled-green?style=for-the-badge) ![Automation](https://img.shields.io/badge/Automation-Active-success?style=for-the-badge)

---

## 🚀 **Project Overview**

This project automates the **invoice data entry process** from an Excel file to Google Sheets. Designed for **E-commerce and Retail businesses**, this script eliminates manual data entry, reduces errors, and provides real-time data updates.

✅ **Reads invoice data** (Invoice ID, Date, Customer Name, Total Amount) from an Excel file.  
✅ **Appends new entries** to a Google Sheets document automatically.  
✅ **Prevents duplicate entries** by checking for existing Invoice IDs.  
✅ **Runs with a single command** for seamless updates.  

---

## 🎯 **Project Goals**

- 📚 **Automate repetitive tasks:** Reduce manual effort and errors.  
- 📊 **Enhance data accuracy:** Prevent duplicate or missing entries.  
- ⏱️ **Save time:** Streamline the invoice data entry process.  

---

## ⚡️ **Tech Stack & Tools**

| Technology      | Purpose                                  |
|----------------|------------------------------------------|
| 🐍 Python       | Core scripting language                 |
| 📊 Pandas       | Data manipulation and analysis           |
| 📡 Google Sheets API | Update and manage Google Sheets       |
| 📚 OpenPyXL     | Excel file handling                      |

---

## 📝 **Project Workflow**

### 1️⃣ **Set Up Google Sheets API**  
- Enable Google Sheets API and generate `credentials.json`.  
- Configure API access and connect to Google Sheets.  

### 2️⃣ **Read & Extract Data from Excel**  
- Use `Pandas` and `OpenPyXL` to read invoice data.  
- Extract relevant columns: `Invoice ID`, `Date`, `Customer Name`, and `Total Amount`.  

### 3️⃣ **Send Data to Google Sheets**  
- Authenticate with Google Sheets API.  
- Check for duplicate entries to avoid duplicates.  
- Append only **new invoice entries** to the sheet.  

### 4️⃣ **Test & Run Script**  
- Test with sample invoice data.  
- Verify correct entries and handle potential errors.  

---


---

## 📊 **Project Results**

✅ **95% Reduction in Manual Effort:** From 2 hours to 5 minutes.  
✅ **Eliminated Duplicate Entries:** Maintains data accuracy.  
✅ **Increased Efficiency:** Automated updates with a single click.  

---

## 🧠 **What I Learned**

- 🔥 **API Integration:** Successfully connected Google Sheets with Python.  
- 📊 **Data Manipulation:** Hands-on experience with `Pandas` and `OpenPyXL`.  
- 🚀 **Error Handling & Optimization:** Ensured duplicate prevention and data accuracy.  

---

## 🚀 **Future Improvements**

1. 📡 **Support for Multiple Excel Files:** Batch process multiple invoice files.  
2. 🔄 **Error Notifications:** Send email alerts for failed entries.  
3. 📊 **Summary Report Generation:** Automatically generate a summarized report of invoices.  
4. ⏱️ **Schedule Automation:** Run the script on a predefined schedule using cron jobs.  

---

## 📚 **How to Run the Script**

### 🛠️ **Prerequisites**
- Python 3.10+ installed  
- Required libraries:
```bash
pip install pandas openpyxl gspread google-auth
python automate_invoice.py
```

