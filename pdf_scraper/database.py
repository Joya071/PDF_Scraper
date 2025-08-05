import sqlite3
from datetime import datetime
from pdf_scraper.logger import get_logger

logger = get_logger()
DB_NAME = 'pdf_data.db'


def initialize_database():
    """
    Creates the SQLite database and table if not exists.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS extracted_pdf_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            data TEXT,
            scraped_at TEXT
        )
    """)

    conn.commit()
    conn.close()
    logger.info("Database initialized.")


def save_to_database(filename: str, text: str) -> None:
    """
    Saves extracted PDF text into the database.

    Args:
        filename (str): Name of the PDF file.
        text (str): Extracted text content.
    """

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    scraped_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S")

    try:
        cursor.execute(
            "INSERT INTO extracted_pdf_details (filename, data, scraped_at) VALUES (?, ?, ?)",
            (filename, text, scraped_at)
        )
        conn.commit()
        logger.info("Data saved to database: %s", filename)
    except sqlite3.IntegrityError:
        logger.warning("Skipped (already exists): %s",
                       filename)
    finally:
        conn.close()