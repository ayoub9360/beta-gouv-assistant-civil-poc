export interface StructuredConclusions {
  faits: string[];
  pretentions: string[];
  moyens: string[];
}

export interface PartySummary {
  party: string;
  summary: string;
}

export interface ComparisonReport {
  convergences: string[];
  divergences: string[];
  key_issues: string[];
}

export interface FullAnalysisResponse {
  demandeur: StructuredConclusions;
  defendeur: StructuredConclusions;
  summary_demandeur: PartySummary;
  summary_defendeur: PartySummary;
  comparison: ComparisonReport;
}

export interface ExtractionResult {
  party: string;
  text: string;
}

export interface TestDataResponse {
  demandeur: ExtractionResult;
  defendeur: ExtractionResult;
}
