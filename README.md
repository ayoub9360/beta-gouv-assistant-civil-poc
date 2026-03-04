# Mon Assistant Civil

> Outil d'aide à l'analyse de conclusions juridiques par intelligence artificielle.

## Fonctionnalités

- **Upload** de conclusions PDF (demandeur + défendeur)
- **Extraction structurée** : faits, prétentions, moyens juridiques
- **Résumé synthétique** de chaque partie
- **Rapport comparatif** : convergences, divergences, points clés du litige
- Interface conforme au **Design System de l'État** (DSFR)

## Stack technique

| Composant | Technologie |
|-----------|-------------|
| Frontend | Next.js, TypeScript, react-dsfr |
| Backend | Python 3.12, FastAPI, UV |
| Extraction PDF | PyMuPDF4LLM |
| Analyse IA | OpenAI GPT-4o |
| Déploiement | Docker Compose |

## Prérequis

- Docker et Docker Compose
- Une clé API OpenAI

## Installation et lancement

### Avec Docker Compose (recommandé)

```bash
# Cloner le projet
git clone <repo-url>
cd assistant-civil-ia

# Configurer la clé API
echo "OPENAI_API_KEY=sk-..." > .env

# Lancer les services
docker compose up --build
```

- Frontend : http://localhost:3000
- Backend API : http://localhost:8000
- Documentation API : http://localhost:8000/docs

### Développement local

**Backend :**

```bash
cd backend
echo "OPENAI_API_KEY=sk-..." > .env
uv pip install -e .
uvicorn assistant_civil.main:app --reload
```

**Frontend :**

```bash
cd frontend
pnpm install
pnpm dev
```

## Utilisation

1. Accéder à http://localhost:3000
2. Cliquer sur "Commencer l'analyse"
3. Déposer les conclusions du demandeur (PDF)
4. Déposer les conclusions du défendeur (PDF)
5. Cliquer sur "Lancer l'analyse"
6. Consulter les résultats :
   - **Analyse structurée** : faits, prétentions, moyens par partie
   - **Résumés** : synthèse de chaque position
   - **Rapport comparatif** : convergences, divergences, points clés

## Documents de test

Le dossier `test-data/` contient deux PDF fictifs pour tester le système :
- `conclusions-demandeur.pdf` — Mme MARTIN (vices cachés immobilier)
- `conclusions-defendeur.pdf` — M. BERNARD (défense)

## Architecture

- [Architecture POC](docs/architecture-poc.md) — choix techniques, pipeline, limites
- [Architecture Production](docs/architecture-production.md) — vision avec LLM souverain, ProConnect

## Structure du projet

```
├── docker-compose.yml
├── backend/
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── src/assistant_civil/
│       ├── main.py              # FastAPI app
│       ├── config.py            # Configuration
│       ├── routers/
│       │   ├── upload.py        # POST /api/upload
│       │   └── analysis.py      # POST /api/analyze
│       ├── services/
│       │   ├── pdf_extractor.py # PyMuPDF4LLM
│       │   └── llm_analyzer.py  # Appels LLM
│       ├── models/
│       │   └── schemas.py       # Modèles Pydantic
│       └── prompts/             # Prompts LLM
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   └── src/
│       ├── app/                 # Pages Next.js
│       ├── components/          # Composants DSFR
│       ├── lib/                 # Client API
│       └── types/               # Types TypeScript
├── test-data/                   # PDF fictifs
└── docs/                        # Documentation architecture
```

## API

| Méthode | Route | Description |
|---------|-------|-------------|
| GET | `/api/health` | Health check |
| POST | `/api/upload` | Upload PDF, retourne texte extrait |
| POST | `/api/analyze` | Analyse complète des conclusions |