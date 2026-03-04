# Architecture POC — Mon Assistant Civil

## Vue d'ensemble

```mermaid
graph TB
    subgraph Frontend["Frontend (Next.js)"]
        UI[Interface DSFR]
        Upload[Upload Zone]
        Results[Résultats]
    end

    subgraph Backend["Backend (FastAPI)"]
        API[API REST]
        PDF[PDF Extractor<br/>PyMuPDF4LLM]
        LLM[LLM Analyzer]
    end

    subgraph External["Services externes"]
        OpenAI[OpenAI API<br/>GPT-4o]
    end

    UI --> Upload
    Upload -->|POST /api/upload| API
    API --> PDF
    PDF -->|Texte extrait| API
    API -->|POST /api/analyze| LLM
    LLM -->|3 appels séquentiels| OpenAI
    OpenAI -->|JSON structuré| LLM
    LLM -->|FullAnalysisResponse| API
    API --> Results
    Results --> UI
```

## Stack technique

| Composant | Technologie | Justification |
|-----------|-------------|---------------|
| Frontend | Next.js + react-dsfr | Framework React mature + Design System de l'État |
| Backend | FastAPI (Python 3.12) | Performance async, typage fort, documentation auto |
| Extraction PDF | PyMuPDF4LLM | Conversion PDF → Markdown optimisée pour LLM |
| LLM | OpenAI GPT-4o | Meilleur rapport qualité/prix pour l'analyse juridique |
| Déploiement | Docker Compose | Simplicité, reproductibilité |

## Pipeline d'analyse

```mermaid
sequenceDiagram
    participant U as Utilisateur
    participant F as Frontend
    participant B as Backend
    participant O as OpenAI

    U->>F: Upload 2 PDF
    F->>B: POST /api/upload (demandeur)
    F->>B: POST /api/upload (défendeur)
    B-->>F: Textes extraits

    F->>B: POST /api/analyze
    B->>O: Prompt structure (demandeur)
    O-->>B: JSON faits/prétentions/moyens
    B->>O: Prompt structure (défendeur)
    O-->>B: JSON faits/prétentions/moyens
    B->>O: Prompt résumé (demandeur)
    O-->>B: JSON résumé
    B->>O: Prompt résumé (défendeur)
    O-->>B: JSON résumé
    B->>O: Prompt comparaison
    O-->>B: JSON convergences/divergences
    B-->>F: FullAnalysisResponse

    F-->>U: Affichage résultats
```

## Endpoints API

| Méthode | Route | Description | Input | Output |
|---------|-------|-------------|-------|--------|
| GET | `/api/health` | Health check | - | `{"status": "ok"}` |
| POST | `/api/upload` | Upload PDF | `file` (PDF) + `party` | `ExtractionResult` |
| POST | `/api/analyze` | Analyse complète | `AnalyzeRequest` | `FullAnalysisResponse` |

## Modèle de données

```python
FullAnalysisResponse:
  demandeur: StructuredConclusions    # faits[], prétentions[], moyens[]
  defendeur: StructuredConclusions
  summary_demandeur: PartySummary     # party, summary
  summary_defendeur: PartySummary
  comparison: ComparisonReport        # convergences[], divergences[], key_issues[]
```

## Choix techniques et compromis

### Pourquoi PyMuPDF4LLM ?
- Conversion PDF → Markdown qui préserve la structure du document
- Plus fiable que l'OCR pour les PDF textuels (cas majoritaire pour les conclusions)
- Léger et rapide

### Pourquoi 3 appels LLM séquentiels ?
- Permet des prompts spécialisés et plus précis
- Chaque étape produit un JSON structuré validé par Pydantic
- Facilite le débugage et l'itération sur chaque prompt

### Pourquoi le CSS DSFR via CDN ?
- Compatibilité immédiate avec tous les bundlers
- Pas de problème de compilation SCSS en build time
- Acceptable pour un POC, à internaliser en production

## Limites du POC

1. **Pas de persistence** : aucune base de données, les analyses ne sont pas sauvegardées
2. **Pas d'authentification** : accès libre, pas de gestion des utilisateurs
3. **Dépendance OpenAI** : pas de fallback si l'API est indisponible
4. **PDF uniquement** : pas de support pour d'autres formats de documents
5. **Pas de RAG** : pas de contexte jurisprudentiel enrichi
6. **Pas de cache** : chaque analyse refait les appels LLM
7. **Prompts fixes** : pas de personnalisation par type d'affaire
