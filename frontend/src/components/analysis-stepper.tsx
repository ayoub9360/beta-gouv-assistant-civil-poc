"use client";

import { Stepper } from "@codegouvfr/react-dsfr/Stepper";

const STEPS = [
  { title: "Import des documents", next: "Extraction du texte" },
  { title: "Extraction du texte", next: "Analyse par IA" },
  { title: "Analyse par IA", next: "Résultats" },
  { title: "Résultats", next: undefined },
];

interface AnalysisStepperProps {
  currentStep: number;
}

export function AnalysisStepper({ currentStep }: AnalysisStepperProps) {
  const step = STEPS[currentStep - 1];

  return (
    <Stepper
      currentStep={currentStep}
      stepCount={STEPS.length}
      title={step?.title ?? ""}
      nextTitle={step?.next}
    />
  );
}
