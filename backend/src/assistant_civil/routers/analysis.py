from fastapi import APIRouter, HTTPException

from assistant_civil.models.schemas import AnalyzeRequest, FullAnalysisResponse
from assistant_civil.services.llm_analyzer import (
    compare_conclusions,
    structure_conclusions,
    summarize_conclusions,
)

router = APIRouter(prefix="/api")


@router.post("/analyze", response_model=FullAnalysisResponse)
async def analyze_conclusions(request: AnalyzeRequest):
    try:
        # Étape 1 : extraction structurée (en parallèle pour les 2 parties)
        demandeur_struct = await structure_conclusions(
            request.demandeur_text, "demandeur"
        )
        defendeur_struct = await structure_conclusions(
            request.defendeur_text, "défendeur"
        )

        # Étape 2 : résumés (en parallèle pour les 2 parties)
        summary_demandeur = await summarize_conclusions(
            request.demandeur_text, "demandeur"
        )
        summary_defendeur = await summarize_conclusions(
            request.defendeur_text, "défendeur"
        )

        # Étape 3 : comparaison
        comparison = await compare_conclusions(
            request.demandeur_text, request.defendeur_text
        )

        return FullAnalysisResponse(
            demandeur=demandeur_struct,
            defendeur=defendeur_struct,
            summary_demandeur=summary_demandeur,
            summary_defendeur=summary_defendeur,
            comparison=comparison,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'analyse : {e}")
