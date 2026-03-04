from pathlib import Path

from fastapi import APIRouter, File, Form, UploadFile, HTTPException

from assistant_civil.models.schemas import ExtractionResult, TestDataResponse
from assistant_civil.services.pdf_extractor import extract_pdf_to_markdown

router = APIRouter(prefix="/api")

import os

TEST_DATA_DIR = Path(os.environ.get("TEST_DATA_DIR", Path(__file__).resolve().parents[4] / "test-data"))


@router.post("/upload", response_model=ExtractionResult)
async def upload_pdf(
    file: UploadFile = File(...),
    party: str = Form(...),
):
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Seuls les fichiers PDF sont acceptés.")

    if party not in ("demandeur", "defendeur"):
        raise HTTPException(status_code=400, detail="Le champ party doit être 'demandeur' ou 'defendeur'.")

    pdf_bytes = await file.read()
    if len(pdf_bytes) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Le fichier ne doit pas dépasser 10 Mo.")

    try:
        text = extract_pdf_to_markdown(pdf_bytes)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erreur lors de l'extraction du PDF : {e}")

    return ExtractionResult(party=party, text=text)


@router.get("/test-data", response_model=TestDataResponse)
async def load_test_data():
    demandeur_path = TEST_DATA_DIR / "conclusions-demandeur.pdf"
    defendeur_path = TEST_DATA_DIR / "conclusions-defendeur.pdf"

    if not demandeur_path.exists() or not defendeur_path.exists():
        raise HTTPException(status_code=404, detail="Fichiers de test introuvables.")

    try:
        demandeur_text = extract_pdf_to_markdown(demandeur_path.read_bytes())
        defendeur_text = extract_pdf_to_markdown(defendeur_path.read_bytes())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur extraction test data : {e}")

    return TestDataResponse(
        demandeur=ExtractionResult(party="demandeur", text=demandeur_text),
        defendeur=ExtractionResult(party="defendeur", text=defendeur_text),
    )
