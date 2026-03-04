"use client";

import { Header } from "@codegouvfr/react-dsfr/Header";

export function AppHeader() {
  return (
    <Header
      brandTop={
        <>
          RÉPUBLIQUE
          <br />
          FRANÇAISE
        </>
      }
      serviceTitle="Mon Assistant Civil"
      serviceTagline="Analyse de conclusions juridiques par IA"
      homeLinkProps={{ href: "/", title: "Accueil — Mon Assistant Civil" }}
      navigation={[
        { text: "Accueil", linkProps: { href: "/" } },
        { text: "Analyse", linkProps: { href: "/analyse" } },
      ]}
    />
  );
}
