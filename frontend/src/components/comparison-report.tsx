"use client";

import { Badge } from "@codegouvfr/react-dsfr/Badge";
import type { ComparisonReport } from "@/types/analysis";

interface ComparisonReportViewProps {
  comparison: ComparisonReport;
}

export function ComparisonReportView({
  comparison,
}: ComparisonReportViewProps) {
  return (
    <div>
      <h3>Rapport comparatif</h3>

      <div className="fr-table">
        <table>
          <thead>
            <tr>
              <th>Type</th>
              <th>Détail</th>
            </tr>
          </thead>
          <tbody>
            {comparison.convergences.map((item, i) => (
              <tr key={`conv-${i}`}>
                <td>
                  <Badge severity="success">Convergence</Badge>
                </td>
                <td>{item}</td>
              </tr>
            ))}
            {comparison.divergences.map((item, i) => (
              <tr key={`div-${i}`}>
                <td>
                  <Badge severity="error">Divergence</Badge>
                </td>
                <td>{item}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <h4 className="fr-mt-3w">
        <span className="fr-icon-warning-line fr-mr-1w" aria-hidden="true" />
        Points clés du litige
      </h4>
      <ul>
        {comparison.key_issues.map((issue, i) => (
          <li key={i} className="fr-mb-1w">
            <strong>{issue}</strong>
          </li>
        ))}
      </ul>
    </div>
  );
}
