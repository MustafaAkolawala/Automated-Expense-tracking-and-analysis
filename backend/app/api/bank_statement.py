from fastapi import APIRouter, File, UploadFile
from app.services.ocr_service import extract_text_from_image, extract_text_from_pdf
from app.services.nlp_service import analyze_statement

router = APIRouter()

@router.post("/upload-statement")
async def upload_statement(file: UploadFile = File(...)):
    if file.content_type == "application/pdf":
        content = extract_text_from_pdf(file.filename)
    else:
        content = extract_text_from_image(file.filename)
    
    extracted_expenses = analyze_statement(content)
    return {"expenses": extracted_expenses}
