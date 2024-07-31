import fitz  # PyMuPDF
import json

def extract_text_from_pdf(pdf_path):
    with fitz.open(pdf_path) as pdf:
        text = ""
        for page_num in range(pdf.page_count):
            page = pdf.load_page(page_num)
            text += page.get_text()
    return text

pdf_files = [r"C:/Users/Abhinay singh/Desktop/chatbot python/Procurement deatils 2023-24.pdf"]

pdf_data = {}
for pdf_file in pdf_files:
    pdf_data[pdf_file] = extract_text_from_pdf(pdf_file)

with open("pdf_data.json", 'w') as f:
    json.dump(pdf_data, f)
