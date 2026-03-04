import { createGetHtmlAttributes } from "@codegouvfr/react-dsfr/next-app-router/getHtmlAttributes";
import { StartDsfrOnHydration } from "./start-dsfr";
import { DsfrProvider } from "./dsfr-provider";
import { DsfrHeadWrapper } from "./dsfr-head";
import { AppHeader } from "./app-header";
import { AppFooter } from "./app-footer";

const defaultColorScheme = "light" as const;

const { getHtmlAttributes } = createGetHtmlAttributes({ defaultColorScheme });

export const metadata = {
  title: "Mon Assistant Civil — Analyse de conclusions juridiques",
  description:
    "Outil d'aide à l'analyse de conclusions juridiques par intelligence artificielle",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html {...getHtmlAttributes({ lang: "fr" })}>
      <head>
        <StartDsfrOnHydration />
        <DsfrHeadWrapper />
      </head>
      <body>
        <DsfrProvider lang="fr">
          <AppHeader />
          <main className="fr-container fr-my-4w">{children}</main>
          <AppFooter />
        </DsfrProvider>
      </body>
    </html>
  );
}
