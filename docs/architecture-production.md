# Architecture Production — Mon Assistant Civil

## Vision

Transformer le POC en plateforme robuste, souveraine et scalable pour l'analyse de conclusions juridiques civiles au sein du système judiciaire français.

## Architecture cible

```mermaid
graph TB
    subgraph Clients["Clients"]
        Web[Navigateur Web]
        API_Client[Clients API]
    end

    subgraph Auth["Authentification"]
        ProConnect[ProConnect SSO]
    end

    subgraph Frontend["Frontend (Next.js)"]
        DSFR[Interface DSFR]
        Templates[Gestion templates]
    end

    subgraph API_Gateway["API Gateway"]
        Nginx[Nginx / Traefik]
        RateLimit[Rate Limiting]
    end

    subgraph Backend["Backend (FastAPI)"]
        REST[API REST]
        Workers[Workers async]
        Cache_Layer[Cache Layer]
    end

    subgraph LLM_Layer["Couche LLM"]
        Strategy[Pattern Strategy]
        Albert[Albert / LLM État]
        Ollama[Ollama<br/>Mistral / Llama]
    end

    subgraph Storage["Stockage"]
        PostgreSQL[(PostgreSQL)]
        MinIO[(MinIO<br/>Stockage objet)]
        Redis[(Redis<br/>Cache + Queue)]
    end

    subgraph Monitoring["Observabilité"]
        Prometheus[Prometheus]
        Grafana[Grafana]
        Logs[Loki / ELK]
    end

    Web --> ProConnect
    API_Client --> API_Gateway
    ProConnect --> Frontend
    Frontend --> API_Gateway
    API_Gateway --> Backend
    Backend --> Cache_Layer
    Cache_Layer --> Redis
    Backend --> Workers
    Workers --> Strategy
    Strategy --> Albert
    Strategy --> Ollama
    Backend --> PostgreSQL
    Backend --> MinIO
    Backend --> Prometheus
    Prometheus --> Grafana
```

## Composants clés

### 1. LLM souverain — Pattern Strategy

```python
class LLMProvider(Protocol):
    async def complete(self, prompt: str) -> str: ...

class AlbertProvider(LLMProvider):
    """LLM de l'État français — prioritaire"""

class OllamaProvider(LLMProvider):
    """Ollama local (Mistral/Llama) — fallback souverain"""

class LLMService:
    def __init__(self, providers: list[LLMProvider]):
        self.providers = providers

    async def complete(self, prompt: str) -> str:
        for provider in self.providers:
            try:
                return await provider.complete(prompt)
            except Exception:
                continue
        raise LLMUnavailableError()
```

**Stratégie de migration** :
1. Phase 1 (POC) : OpenAI GPT-4o pour la démonstration de faisabilité
2. Phase 2 : Migration vers Ollama (Mistral/Llama) en local
3. Phase 3 : Migration vers Albert (LLM État) quand disponible en production

### 2. Authentification — ProConnect

- SSO de l'État français (successeur de FranceConnect Agent)
- Authentification des greffiers, magistrats, avocats
- Gestion des rôles et permissions par juridiction
- Conformité RGPD et référentiel RGS

### 3. Persistence et stockage

| Donnée | Stockage | Justification |
|--------|----------|---------------|
| Utilisateurs, sessions | PostgreSQL | Données relationnelles structurées |
| Analyses, historique | PostgreSQL | Traçabilité et audit |
| Documents PDF | MinIO | Stockage objet S3-compatible, souverain |
| Cache, sessions | Redis | Performance, TTL natif |
| Queue de tâches | Redis (ou RabbitMQ) | Traitement async des analyses longues |

### 4. Templates de prompts

```python
class PromptTemplate:
    id: UUID
    name: str
    jurisdiction_type: str  # TJ, CA, Cour de cassation
    case_type: str          # vices cachés, bail, divorce...
    structure_prompt: str
    summary_prompt: str
    comparison_prompt: str
    created_by: UUID
    version: int
```

- Templates personnalisables par juridiction et type d'affaire
- Versionnement des prompts avec historique
- Interface d'administration pour les référents
- A/B testing possible entre versions de prompts

### 5. Infrastructure

```mermaid
graph TB
    subgraph Production["Cluster Kubernetes"]
        subgraph Ingress
            Traefik[Traefik Ingress]
        end

        subgraph App["Application"]
            FE[Frontend x2]
            BE[Backend x3]
            Worker[Workers x2]
        end

        subgraph Data["Données"]
            PG[(PostgreSQL HA)]
            Redis_Cluster[(Redis Sentinel)]
            MinIO_Cluster[(MinIO Cluster)]
        end

        subgraph LLM["LLM"]
            Ollama_GPU[Ollama<br/>GPU Node]
        end

        subgraph Obs["Observabilité"]
            Prom[Prometheus]
            Graf[Grafana]
            Loki[Loki]
        end
    end

    Traefik --> FE
    Traefik --> BE
    BE --> Worker
    BE --> PG
    BE --> Redis_Cluster
    Worker --> Ollama_GPU
    Worker --> PG
    Worker --> MinIO_Cluster
    BE --> Prom
    Prom --> Graf
```

**Options d'hébergement souverain** :
- OVHcloud (SecNumCloud)
- Outscale (SecNumCloud)
- Cloud interne du Ministère de la Justice

**Scaling** :
- Frontend : réplicas stateless, CDN pour assets
- Backend : scaling horizontal, workers async pour les analyses LLM
- LLM : GPU dédié(s) pour Ollama, scaling vertical
- PostgreSQL : réplication streaming, pgBouncer pour le pooling
