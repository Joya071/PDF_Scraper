import os
from pdf_scraper.extractor import extract_text_from_pdf
from pdf_scraper.database import save_to_database
from pdf_scraper.logger import get_logger

logger = get_logger()


def process_pdfs_in_directory(directory: str, output_file: str) -> None:
    """
    Extracts text from all PDFs in a given directory and saves it to an output file.

    This function scans a directory for all `.pdf` files, extracts their text content,
    and writes the extracted text into a specified output file.

    Args:
        directory (str): The path to the directory containing PDF files.
        output_file (str): The file path where extracted text will be saved.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        PermissionError: If there are permission issues accessing files.
        RuntimeError: If an error occurs while extracting text from a PDF.

    Example:
        >>> process_pdfs_in_directory("pdf_folder", "output.txt")
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")

    # Get all PDFs in the directory
    pdf_files = [f for f in os.listdir(
        directory) if f.lower().endswith('.pdf')]

    # Stop execution if no PDFs are found
    if not pdf_files:
        logger.warning(
            "No PDF files found in the directory: %s. Exiting.", directory)
        return  # Stop execution

    with open(output_file, "w", encoding="utf-8") as out_file:
        for filename in pdf_files:
            pdf_path = os.path.join(directory, filename)
            logger.info("Processing the PDF: %s", filename)

            try:
                extracted_text = extract_text_from_pdf(pdf_path)
                out_file.write(f"---- {filename} ----\n{extracted_text}\n\n")
                save_to_database(filename, extracted_text)
            except Exception as e:
                logger.error("Error processing %s: %s", filename, e)

    logger.info("PDF processing completed")