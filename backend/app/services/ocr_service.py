import pytesseract
from PIL import Image
from io import BytesIO
from pdf2image import convert_from_bytes


def extract_text_from_image(image_bytes: bytes):
    image = Image.open(BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf(pdf_bytes: bytes):
    images = convert_from_bytes(pdf_bytes)
    
    extracted_text = ""
    for page_image in images:
        text = pytesseract.image_to_string(page_image)
        extracted_text += text + "\n"  
    return extracted_text