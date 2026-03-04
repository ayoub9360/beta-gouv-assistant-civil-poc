"use client";

import { Footer } from "@codegouvfr/react-dsfr/Footer";

export function AppFooter() {
  return (
    <Footer
      accessibility="non compliant"
      accessibilityLinkProps={{ href: "#" }}
      contentDescription="Mon Assistant Civil est un outil expérimental d'aide à l'analyse de conclusions juridiques, développé dans le cadre du programme beta.gouv.fr."
      bottomItems={[
        {
          text: "Mentions légales",
          linkProps: { href: "#" },
        },
      ]}
    />
  );
}
