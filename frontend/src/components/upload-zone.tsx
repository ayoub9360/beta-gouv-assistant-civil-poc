"use client";

import { Upload } from "@codegouvfr/react-dsfr/Upload";
import { Alert } from "@codegouvfr/react-dsfr/Alert";
import { Button } from "@codegouvfr/react-dsfr/Button";

interface UploadZoneProps {
  onFilesReady: (demandeur: File, defendeur: File) => void;
  isLoading: boolean;
  demandeurFile: File | null;
  defendeurFile: File | null;
  onDemandeurChange: (file: File | null) => void;
  onDefendeurChange: (file: File | null) => void;
}

export function UploadZone({
  onFilesReady,
  isLoading,
  demandeurFile,
  defendeurFile,
  onDemandeurChange,
  onDefendeurChange,
}: UploadZoneProps) {
  const handleSubmit = () => {
    if (demandeurFile && defendeurFile) {
      onFilesReady(demandeurFile, defendeurFile);
    }
  };

  return (
    <div>
      <Alert
        severity="info"
        small
        description="Déposez les conclusions de chaque partie au format PDF (max 10 Mo par fichier)."
        className="fr-mb-3w"
      />

      <div className="fr-grid-row fr-grid-row--gutters">
        <div className="fr-col-12 fr-col-md-6">
          <Upload
            label="Conclusions du demandeur"
            hint="Format PDF uniquement"
            nativeInputProps={{
              accept: ".pdf",
              onChange: (e) => {
                const file = e.target.files?.[0] ?? null;
                onDemandeurChange(file);
              },
            }}
            state={demandeurFile ? "default" : "default"}
            stateRelatedMessage={
              demandeurFile ? `Fichier : ${demandeurFile.name}` : undefined
            }
          />
        </div>
        <div className="fr-col-12 fr-col-md-6">
          <Upload
            label="Conclusions du défendeur"
            hint="Format PDF uniquement"
            nativeInputProps={{
              accept: ".pdf",
              onChange: (e) => {
                const file = e.target.files?.[0] ?? null;
                onDefendeurChange(file);
              },
            }}
            state={defendeurFile ? "default" : "default"}
            stateRelatedMessage={
              defendeurFile ? `Fichier : ${defendeurFile.name}` : undefined
            }
          />
        </div>
      </div>

      <div className="fr-mt-3w" style={{ textAlign: "center" }}>
        <Button
          onClick={handleSubmit}
          disabled={!demandeurFile || !defendeurFile || isLoading}
          iconId="fr-icon-search-line"
          iconPosition="right"
        >
          {isLoading ? "Extraction en cours..." : "Lancer l'analyse"}
        </Button>
      </div>
    </div>
  );
}
