FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy project files
COPY backend/pyproject.toml .
COPY backend/src/ src/

# Copy test data
COPY test-data/ /data/test-data/

# Install dependencies
RUN uv pip install --system --no-cache .

EXPOSE 8000

CMD ["uvicorn", "assistant_civil.main:app", "--host", "0.0.0.0", "--port", "8000"]
