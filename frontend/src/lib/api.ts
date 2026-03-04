import type { ExtractionResult, FullAnalysisResponse, TestDataResponse } from "@/types/analysis";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function uploadPdf(
  file: File,
  party: "demandeur" | "defendeur",
): Promise<ExtractionResult> {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("party", party);

  const response = await fetch(`${API_BASE}/api/upload`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: "Erreur inconnue" }));
    throw new Error(error.detail || `Erreur ${response.status}`);
  }

  return response.json();
}

export async function analyzeConclusions(
  demandeurText: string,
  defendeurText: string,
): Promise<FullAnalysisResponse> {
  const response = await fetch(`${API_BASE}/api/analyze`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      demandeur_text: demandeurText,
      defendeur_text: defendeurText,
    }),
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: "Erreur inconnue" }));
    throw new Error(error.detail || `Erreur ${response.status}`);
  }

  return response.json();
}

export async function loadTestData(): Promise<TestDataResponse> {
  const response = await fetch(`${API_BASE}/api/test-data`);

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: "Erreur inconnue" }));
    throw new Error(error.detail || `Erreur ${response.status}`);
  }

  return response.json();
}
