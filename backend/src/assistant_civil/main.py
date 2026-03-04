from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from assistant_civil.config import settings
from assistant_civil.routers import upload, analysis

app = FastAPI(
    title="Mon Assistant Civil",
    description="API d'analyse de conclusions juridiques par IA",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(analysis.router)


@app.get("/api/health")
async def health_check():
    return {"status": "ok"}
