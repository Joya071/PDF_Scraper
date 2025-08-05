import argparse
import os
from pdf_scraper.processor import process_pdfs_in_directory
from pdf_scraper.database import initialize_database
from pdf_scraper.logger import get_logger
logger = get_logger()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract text from all PDFs in a directory")
    parser.add_argument(
        "directory", help="Path to the directory containing PDFs")
    parser.add_argument("output", help="Output file to save extracted text")

    args = parser.parse_args()

    if not os.path.exists(args.directory):
        logger.error("Error: Directory does not exists! %s", args.directory)
    else:
        logger.info("Starting PDF processing for directory: %s",
                    args.directory)
        initialize_database()
        process_pdfs_in_directory(args.directory, args.output)
        logger.info("Processing complete.")