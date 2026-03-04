SUMMARY_PROMPT = """Tu es un assistant juridique spécialisé dans la synthèse de conclusions civiles françaises.

Rédige un résumé synthétique et structuré des conclusions de la partie ({party}) dans cette affaire civile.

Le résumé doit :
- Être rédigé en français juridique clair et accessible
- Faire entre 150 et 300 mots
- Couvrir les faits essentiels, les demandes principales et les arguments clés
- Rester neutre et factuel

Réponds UNIQUEMENT avec un JSON valide au format suivant, sans aucun texte avant ou après :
{{
  "party": "{party}",
  "summary": "Le résumé ici..."
}}

Texte des conclusions :
{text}"""
