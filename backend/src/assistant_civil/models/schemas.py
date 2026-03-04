from pydantic import BaseModel


class ExtractionResult(BaseModel):
    party: str
    text: str


class StructuredConclusions(BaseModel):
    faits: list[str]
    pretentions: list[str]
    moyens: list[str]


class PartySummary(BaseModel):
    party: str
    summary: str


class ComparisonReport(BaseModel):
    convergences: list[str]
    divergences: list[str]
    key_issues: list[str]


class FullAnalysisResponse(BaseModel):
    demandeur: StructuredConclusions
    defendeur: StructuredConclusions
    summary_demandeur: PartySummary
    summary_defendeur: PartySummary
    comparison: ComparisonReport


class AnalyzeRequest(BaseModel):
    demandeur_text: str
    defendeur_text: str


class TestDataResponse(BaseModel):
    demandeur: ExtractionResult
    defendeur: ExtractionResult
