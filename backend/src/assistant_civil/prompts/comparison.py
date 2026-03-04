COMPARISON_PROMPT = """Tu es un assistant juridique spécialisé dans l'analyse comparative de conclusions civiles françaises.

Compare les conclusions des deux parties dans cette affaire civile et produis un rapport structuré.

**Conclusions du demandeur :**
{demandeur_text}

**Conclusions du défendeur :**
{defendeur_text}

Analyse et identifie :

1. **Convergences** : Les points sur lesquels les deux parties s'accordent (faits reconnus, points non contestés)
2. **Divergences** : Les points de désaccord (faits contestés, interprétations contradictoires, demandes opposées)
3. **Points clés du litige** : Les questions essentielles que le tribunal devra trancher

Réponds UNIQUEMENT avec un JSON valide au format suivant, sans aucun texte avant ou après :
{{
  "convergences": ["point de convergence 1", "point de convergence 2", ...],
  "divergences": ["point de divergence 1", "point de divergence 2", ...],
  "key_issues": ["question clé 1", "question clé 2", ...]
}}"""
