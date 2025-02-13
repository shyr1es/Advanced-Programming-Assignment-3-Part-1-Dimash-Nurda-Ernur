import pdfplumber

def extract_text_from_pdf(pdf_file):
    """Извлечение текста из PDF."""
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text
