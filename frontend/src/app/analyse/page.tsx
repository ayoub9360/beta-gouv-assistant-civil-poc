"use client";

import { AnalysisStepper } from "@/components/analysis-stepper";
import { ComparisonReportView } from "@/components/comparison-report";
import { StructuredView } from "@/components/structured-view";
import { SummaryCards } from "@/components/summary-card";
import { UploadZone } from "@/components/upload-zone";
import { analyzeConclusions, loadTestData, uploadPdf } from "@/lib/api";
import type { FullAnalysisResponse } from "@/types/analysis";
import { Alert } from "@codegouvfr/react-dsfr/Alert";
import { Button } from "@codegouvfr/react-dsfr/Button";
import { useState } from "react";

type AnalysisStep = 1 | 2 | 3 | 4;

export default function AnalysePage() {
  const [step, setStep] = useState<AnalysisStep>(1);
  const [demandeurFile, setDemandeurFile] = useState<File | null>(null);
  const [defendeurFile, setDefendeurFile] = useState<File | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<FullAnalysisResponse | null>(null);

  const handleTestData = async () => {
    setIsLoading(true);
    setError(null);

    try {
      setStep(2);
      const testData = await loadTestData();

      setStep(3);
      const analysis = await analyzeConclusions(
        testData.demandeur.text,
        testData.defendeur.text,
      );

      setResult(analysis);
      setStep(4);
    } catch (err) {
      setError(
        err instanceof Error ? err.message : "Une erreur est survenue.",
      );
      setStep(1);
    } finally {
      setIsLoading(false);
    }
  };

  const handleFilesReady = async (demandeur: File, defendeur: File) => {
    setIsLoading(true);
    setError(null);

    try {
      // Étape 2 : extraction du texte
      setStep(2);
      const [demandeurResult, defendeurResult] = await Promise.all([
        uploadPdf(demandeur, "demandeur"),
        uploadPdf(defendeur, "defendeur"),
      ]);

      // Étape 3 : analyse LLM
      setStep(3);
      const analysis = await analyzeConclusions(
        demandeurResult.text,
        defendeurResult.text,
      );

      setResult(analysis);
      setStep(4);
    } catch (err) {
      setError(
        err instanceof Error ? err.message : "Une erreur est survenue.",
      );
      setStep(1);
    } finally {
      setIsLoading(false);
    }
  };

  const handleReset = () => {
    setStep(1);
    setDemandeurFile(null);
    setDefendeurFile(null);
    setResult(null);
    setError(null);
  };

  return (
    <div>
      <h1>Analyse des conclusions</h1>

      <AnalysisStepper currentStep={step} />

      {error && (
        <Alert
          severity="error"
          title="Erreur"
          description={error}
          closable
          onClose={() => setError(null)}
          className="fr-mb-3w"
        />
      )}

      {step === 1 && (
        <>
          <UploadZone
            onFilesReady={handleFilesReady}
            isLoading={isLoading}
            demandeurFile={demandeurFile}
            defendeurFile={defendeurFile}
            onDemandeurChange={setDemandeurFile}
            onDefendeurChange={setDefendeurFile}
          />

          <div className="fr-mt-4w" style={{ textAlign: "center" }}>
            <p className="fr-text--sm fr-mb-1w" style={{ color: "var(--text-mention-grey)" }}>
              — ou —
            </p>
            <Button
              priority="tertiary"
              onClick={handleTestData}
              disabled={isLoading}
              iconId="fr-icon-test-tube-line"
              iconPosition="left"
            >
              Charger des documents de test
            </Button>
          </div>
        </>
      )}

      {(step === 2 || step === 3) && (
        <div className="fr-mt-4w" style={{ textAlign: "center" }}>
          <div className="fr-mb-2w">
            <span
              className="fr-icon-loader-line fr-mr-1w"
              aria-hidden="true"
            />
            {step === 2
              ? "Extraction du texte des PDF en cours..."
              : "Analyse par intelligence artificielle en cours... Cela peut prendre jusqu'à 2 minutes."}
          </div>
          <progress
            className="fr-progress"
            style={{ width: "100%", maxWidth: 400 }}
          />
        </div>
      )}

      {step === 4 && result && (
        <div>
          <StructuredView
            demandeur={result.demandeur}
            defendeur={result.defendeur}
          />

          <hr className="fr-mt-4w fr-mb-4w" />

          <SummaryCards
            summaryDemandeur={result.summary_demandeur}
            summaryDefendeur={result.summary_defendeur}
          />

          <hr className="fr-mt-4w fr-mb-4w" />

          <ComparisonReportView comparison={result.comparison} />

          <div className="fr-mt-4w" style={{ textAlign: "center" }}>
            <Button
              priority="secondary"
              onClick={handleReset}
              iconId="fr-icon-refresh-line"
              iconPosition="left"
            >
              Nouvelle analyse
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}
