import fitz
from pdf_scraper.logger import get_logger


logger = get_logger()


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file.

    This function takes the file path of a PDF, processes it using PyMuPDF (fitz),
    and returns the extracted text from all pages.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file path is invalid.
        RuntimeError: If there is an error while processing the PDF.

    Example:
        >>> text = extract_text_from_pdf("sample.pdf")
        >>> print(text)
    """
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text("text") + "\n"
        logger.info("Extracted text from: %s", pdf_path)
    except FileNotFoundError as e:
        logger.error("File not found error while processings %s: %s",
                     pdf_path, e)
        raise FileNotFoundError(f"File not found: {pdf_path}") from e
    except ValueError as e:
        logger.error("Value error while processings %s: %s", pdf_path, e)
        raise ValueError(f"Invalid file path: {pdf_path}") from e
    except Exception as e:
        logger.error("Error processings %s: %s", pdf_path, e)
        raise RuntimeError(f"Error processing {pdf_path}: {e}") from e

    return text