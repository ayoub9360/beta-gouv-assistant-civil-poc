import json

from openai import AsyncOpenAI

from assistant_civil.config import settings
from assistant_civil.models.schemas import (
    ComparisonReport,
    PartySummary,
    StructuredConclusions,
)
from assistant_civil.prompts.comparison import COMPARISON_PROMPT
from assistant_civil.prompts.structure import STRUCTURE_PROMPT
from assistant_civil.prompts.summary import SUMMARY_PROMPT


def _get_client() -> AsyncOpenAI:
    return AsyncOpenAI(api_key=settings.openai_api_key)


async def _call_llm(prompt: str) -> str:
    client = _get_client()
    response = await client.chat.completions.create(
        model=settings.openai_model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        timeout=60,
    )
    return response.choices[0].message.content or ""


def _parse_json(raw: str) -> dict:
    """Parse le JSON depuis la réponse LLM, en nettoyant les éventuels blocs markdown."""
    cleaned = raw.strip()
    if cleaned.startswith("```"):
        lines = cleaned.split("\n")
        lines = lines[1:]  # retirer ```json
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        cleaned = "\n".join(lines)
    return json.loads(cleaned)


async def structure_conclusions(text: str, party: str) -> StructuredConclusions:
    prompt = STRUCTURE_PROMPT.format(party=party, text=text)
    raw = await _call_llm(prompt)
    data = _parse_json(raw)
    return StructuredConclusions(**data)


async def summarize_conclusions(text: str, party: str) -> PartySummary:
    prompt = SUMMARY_PROMPT.format(party=party, text=text)
    raw = await _call_llm(prompt)
    data = _parse_json(raw)
    return PartySummary(**data)


async def compare_conclusions(
    demandeur_text: str, defendeur_text: str
) -> ComparisonReport:
    prompt = COMPARISON_PROMPT.format(
        demandeur_text=demandeur_text, defendeur_text=defendeur_text
    )
    raw = await _call_llm(prompt)
    data = _parse_json(raw)
    return ComparisonReport(**data)
