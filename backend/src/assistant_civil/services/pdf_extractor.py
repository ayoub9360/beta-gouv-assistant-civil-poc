import pymupdf4llm


def extract_pdf_to_markdown(pdf_bytes: bytes) -> str:
    """Extrait le contenu d'un PDF en Markdown via PyMuPDF4LLM."""
    import tempfile
    import os

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(pdf_bytes)
        tmp_path = tmp.name

    try:
        md_text = pymupdf4llm.to_markdown(tmp_path)
        return md_text
    finally:
        os.unlink(tmp_path)
