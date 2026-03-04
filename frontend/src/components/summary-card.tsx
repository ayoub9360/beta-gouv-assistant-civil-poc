"use client";

import type { PartySummary } from "@/types/analysis";

interface SummaryCardsProps {
  summaryDemandeur: PartySummary;
  summaryDefendeur: PartySummary;
}

export function SummaryCards({
  summaryDemandeur,
  summaryDefendeur,
}: SummaryCardsProps) {
  return (
    <div>
      <h3>Résumés synthétiques</h3>
      <div className="fr-grid-row fr-grid-row--gutters">
        <div className="fr-col-12 fr-col-md-6">
          <div className="fr-card">
            <div className="fr-card__body">
              <div className="fr-card__content">
                <h4 className="fr-card__title">
                  <span
                    className="fr-icon-user-line fr-mr-1w"
                    aria-hidden="true"
                  />
                  Demandeur
                </h4>
                <p className="fr-card__desc">{summaryDemandeur.summary}</p>
              </div>
            </div>
          </div>
        </div>
        <div className="fr-col-12 fr-col-md-6">
          <div className="fr-card">
            <div className="fr-card__body">
              <div className="fr-card__content">
                <h4 className="fr-card__title">
                  <span
                    className="fr-icon-user-line fr-mr-1w"
                    aria-hidden="true"
                  />
                  Défendeur
                </h4>
                <p className="fr-card__desc">{summaryDefendeur.summary}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
