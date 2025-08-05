
# 📄 PDF Scraper with Automation

A Python-based tool to automate the extraction of text from PDFs in a given directory and store the content into an SQLite database for structured access and querying.

---

## 📌 Project Overview

This project automates the extraction of text from machine-readable PDFs and stores the content into an SQLite database. It provides a command-line interface (CLI) and uses modular Python code to ensure flexibility, readability, and reusability.

---

## 🎯 Features

- ✅ Automatically scans and processes all PDFs in a directory
- ✅ Extracts text using PyMuPDF for fast and accurate parsing
- ✅ Stores extracted content in a structured SQLite database
- ✅ Provides CLI-based execution for ease of use
- ✅ Modular architecture for maintainability
- ✅ Logging system to track progress and errors

---

## 🛠️ Why PyMuPDF?

**PyMuPDF** (also known as `fitz`) was chosen over other PDF libraries like `PyPDF2` or `PDFMiner` due to:

- ⚡ **Speed & Efficiency** – much faster processing
- 🧠 **Accuracy** – better layout and structure retention
- 💾 **Lightweight** – less memory consumption
- 📚 **Advanced PDF Support** – handles fonts, styles, and layouts

---

## 📄 Supported PDF Types

| PDF Type                   | Supported          |
| -------------------------- | ------------------ |
| Digitally Generated PDFs   | ✅                 |
| Machine-Readable PDFs      | ✅                 |
| Scanned PDFs (image-based) | ❌ (no OCR)        |
| Encrypted PDFs             | ❌ (if restricted) |

---

## 🚫 Limitations

- ❌ **Scanned PDFs** – No built-in OCR; needs Tesseract or similar
- ❌ **Password-Protected PDFs** – Only supported if permissions allow
- ⚠️ **Complex Layouts** – May struggle with heavy formatting

---

## 📑 Logging System

Logs each step of the extraction and database storage process.

- 🔍 INFO – Normal operations
- ⚠️ WARNING – Non-critical issues (e.g., duplicate file detection)
- ❌ ERROR – File read issues or processing errors

All logs are saved in `scraper.log` for debugging and auditing.

---

## 🤖 Why PDF Text Extraction is Important?

This tool is ideal for:

- 🧪 Data Mining & Research
- 🧾 Invoice or Report Analysis
- 📊 Natural Language Processing (NLP)
- 📚 Searchable Document Archives

---

## 🗂️ Project Structure
```

pdf_scraper/
├── extractor.py # Extracts text from PDFs
├── processor.py # Scans directory and processes PDFs
├── database.py # Handles SQLite database operations
├── logger.py # Manages logging system
├── main.py # CLI entry point
├── requirements.txt # Project dependencies
└── README.md # Project documentation

````

---

## 🚀 Installation & Usage

### 1️⃣ Setup Environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
````

### 2️⃣ Run the Script

```bash
python main.py --directory /path/to/pdf/folder
```

### 3️⃣ Query Extracted Data

Example SQLite query to retrieve content from a specific file:

```sql
SELECT * FROM pdf_text WHERE filename = 'example.pdf';
```

---

## 🧾 Sample Output

| Filename    | Content (truncated)                           |
| ----------- | --------------------------------------------- |
| example.pdf | "This is a sample extracted text from PDF..." |

---

## 📌 Requirements

- Python 3.7+
- PyMuPDF (`fitz`)
- SQLite3
- argparse
- logging

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧠 Future Enhancements

- 🔍 OCR Support using Tesseract for scanned/image PDFs
- 🌐 Web UI for uploading and browsing extracted content
- 📦 Exporting to CSV/JSON formats

---

## 📬 Contact

For questions or suggestions, feel free to connect:
📧 [joyachakraborty072@gmail.com](mailto:joyachakraborty072@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/joya-chakraborty-877525262)

---
