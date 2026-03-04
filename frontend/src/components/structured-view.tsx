"use client";

import { Tabs } from "@codegouvfr/react-dsfr/Tabs";
import { Accordion } from "@codegouvfr/react-dsfr/Accordion";
import type { StructuredConclusions } from "@/types/analysis";

interface StructuredViewProps {
  demandeur: StructuredConclusions;
  defendeur: StructuredConclusions;
}

function ConclusionsAccordions({
  data,
}: {
  data: StructuredConclusions;
}) {
  return (
    <div>
      <Accordion label={`Faits (${data.faits.length})`} defaultExpanded>
        <ul>
          {data.faits.map((fait, i) => (
            <li key={i} className="fr-mb-1w">
              {fait}
            </li>
          ))}
        </ul>
      </Accordion>
      <Accordion label={`Prétentions (${data.pretentions.length})`}>
        <ul>
          {data.pretentions.map((pretention, i) => (
            <li key={i} className="fr-mb-1w">
              {pretention}
            </li>
          ))}
        </ul>
      </Accordion>
      <Accordion label={`Moyens juridiques (${data.moyens.length})`}>
        <ul>
          {data.moyens.map((moyen, i) => (
            <li key={i} className="fr-mb-1w">
              {moyen}
            </li>
          ))}
        </ul>
      </Accordion>
    </div>
  );
}

export function StructuredView({
  demandeur,
  defendeur,
}: StructuredViewProps) {
  return (
    <div>
      <h3>Analyse structurée des conclusions</h3>
      <Tabs
        tabs={[
          {
            label: "Demandeur",
            iconId: "fr-icon-user-line",
            content: <ConclusionsAccordions data={demandeur} />,
            isDefault: true,
          },
          {
            label: "Défendeur",
            iconId: "fr-icon-user-line",
            content: <ConclusionsAccordions data={defendeur} />,
          },
        ]}
      />
    </div>
  );
}
