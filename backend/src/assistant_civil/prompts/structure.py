STRUCTURE_PROMPT = """Tu es un assistant juridique spécialisé dans l'analyse de conclusions civiles françaises.

Analyse le texte suivant qui correspond aux conclusions d'une partie ({party}) dans une affaire civile.

Extrais et structure les informations en trois catégories :

1. **Faits** : Les faits exposés par la partie (événements, dates, circonstances factuelles)
2. **Prétentions** : Les demandes formulées (ce que la partie demande au tribunal — condamnations, dommages-intérêts, etc.)
3. **Moyens** : Les arguments juridiques invoqués (fondements légaux, jurisprudence, raisonnements de droit)

Réponds UNIQUEMENT avec un JSON valide au format suivant, sans aucun texte avant ou après :
{{
  "faits": ["fait 1", "fait 2", ...],
  "pretentions": ["prétention 1", "prétention 2", ...],
  "moyens": ["moyen 1", "moyen 2", ...]
}}

Texte des conclusions :
{text}"""
