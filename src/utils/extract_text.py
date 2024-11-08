import pdfplumber

def extract_text_pdfplumber(pdf_path):
    pages_text = []
    metadatas = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            pages_text.append(page.extract_text())
            metadatas.append({"page_number": page_number, "pdf_path": pdf_path})

    return pages_text, metadatas