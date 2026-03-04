"use client";

import { DsfrProviderBase } from "@codegouvfr/react-dsfr/next-app-router/DsfrProvider";
import Link from "next/link";
import type { ReactNode } from "react";

const defaultColorScheme = "light" as const;

export function DsfrProvider({
  children,
  lang,
}: {
  children: ReactNode;
  lang: string;
}) {
  return (
    <DsfrProviderBase
      lang={lang}
      Link={Link}
      defaultColorScheme={defaultColorScheme}
    >
      {children}
    </DsfrProviderBase>
  );
}
