"""Script pour générer les 2 PDF de test fictifs (conclusions demandeur + défendeur)."""

import fitz  # PyMuPDF


def create_pdf(filename: str, title: str, content: str):
    doc = fitz.open()
    page = doc.new_page()

    # Titre
    page.insert_text(
        fitz.Point(72, 72),
        title,
        fontsize=14,
        fontname="helv",
    )

    # Contenu — insérer par blocs pour gérer les sauts de page
    y = 110
    for line in content.split("\n"):
        if y > 750:
            page = doc.new_page()
            y = 72
        page.insert_text(
            fitz.Point(72, y),
            line,
            fontsize=10,
            fontname="helv",
        )
        y += 14

    doc.save(filename)
    doc.close()
    print(f"Généré : {filename}")


DEMANDEUR = """TRIBUNAL JUDICIAIRE DE PARIS
Chambre civile - Section 5

CONCLUSIONS EN DEMANDE

Affaire n° RG 24/03847

Mme Sophie MARTIN
Demanderesse
Représentée par Maître Claire DUBOIS, avocate au Barreau de Paris

c/

M. Jean BERNARD
Défendeur


PLAISE AU TRIBUNAL

I. RAPPEL DES FAITS

1. Par acte authentique en date du 15 mars 2023, Mme Sophie MARTIN a acquis
auprès de M. Jean BERNARD un appartement situé au 12 rue des Lilas, 75011 Paris,
pour un prix de 385 000 euros.

2. L'acte de vente mentionnait que le bien était en bon état général et ne
présentait aucun désordre apparent. Le diagnostic technique annexé ne signalait
aucune anomalie relative à l'étanchéité.

3. Dès le mois de mai 2023, soit moins de deux mois après la vente,
Mme MARTIN a constaté d'importantes infiltrations d'eau au niveau du mur
porteur de la chambre principale et de la salle de bains.

4. Ces infiltrations ont provoqué l'apparition de moisissures, le décollement
des revêtements muraux et un taux d'humidité anormalement élevé dans les
pièces concernées.

5. Mme MARTIN a mandaté le cabinet d'expertise TECHNI-BATIMENT qui a
rendu son rapport le 20 septembre 2023. L'expert a conclu que les
infiltrations provenaient d'un défaut d'étanchéité de la toiture-terrasse
au-dessus de l'appartement, défaut préexistant à la vente et dissimulé par
des travaux de peinture récents.

6. L'expert a noté la présence de traces d'anciennes réparations sommaires
sur l'étanchéité, démontrant que le vendeur avait connaissance du problème.

7. Le coût des travaux de réparation a été estimé à 62 000 euros pour
la reprise de l'étanchéité et 23 000 euros pour la remise en état des
pièces endommagées, soit un total de 85 000 euros.

8. Par courrier recommandé du 15 octobre 2023, Mme MARTIN a mis en demeure
M. BERNARD de prendre en charge les travaux de réparation. Ce courrier est
resté sans réponse.


II. PRETENTIONS

Mme MARTIN demande au Tribunal de bien vouloir :

- CONSTATER l'existence de vices cachés affectant le bien immobilier vendu ;

- CONDAMNER M. BERNARD au paiement de la somme de 85 000 euros au titre
  des travaux de réparation nécessaires ;

- CONDAMNER M. BERNARD au paiement de la somme de 15 000 euros au titre
  du préjudice de jouissance subi depuis mai 2023 ;

- CONDAMNER M. BERNARD au paiement de la somme de 3 500 euros au titre
  des frais d'expertise ;

- CONDAMNER M. BERNARD aux entiers dépens ainsi qu'au paiement de la
  somme de 5 000 euros au titre de l'article 700 du Code de procédure civile ;

- ORDONNER l'exécution provisoire de la décision à intervenir.


III. MOYENS

A. Sur la garantie des vices cachés (articles 1641 et suivants du Code civil)

Le vice caché est caractérisé dès lors que :
- Le défaut d'étanchéité rend l'appartement impropre à l'usage d'habitation
  normale, les infiltrations provoquant moisissures et dégradations continues ;
- Le vice était antérieur à la vente, comme l'établit le rapport d'expertise
  qui date les désordres à plusieurs années avant la transaction ;
- Le vice était caché, les travaux de peinture réalisés par le vendeur
  ayant précisément pour objet de dissimuler les traces d'infiltration.

B. Sur la connaissance du vice par le vendeur

La mauvaise foi du vendeur est établie par :
- Les traces d'anciennes réparations sommaires constatées par l'expert ;
- Les travaux de peinture récents destinés à masquer les désordres ;
- La durée de sa présence dans les lieux (12 ans) rendant impossible
  l'ignorance des infiltrations récurrentes.

En conséquence, conformément à l'article 1645 du Code civil, le vendeur
de mauvaise foi doit être condamné à tous les dommages et intérêts.

C. Sur le préjudice de jouissance

Depuis mai 2023, Mme MARTIN subit un trouble de jouissance caractérisé
par l'impossibilité d'utiliser normalement les pièces affectées, les
nuisances olfactives liées aux moisissures et l'atteinte à sa santé
(attestation médicale de problèmes respiratoires).

PAR CES MOTIFS, il est demandé au Tribunal de faire droit à l'ensemble
des demandes de Mme MARTIN.

Fait à Paris, le 15 janvier 2024
Maître Claire DUBOIS"""

DEFENDEUR = """TRIBUNAL JUDICIAIRE DE PARIS
Chambre civile - Section 5

CONCLUSIONS EN DEFENSE

Affaire n° RG 24/03847

M. Jean BERNARD
Défendeur
Représenté par Maître François LEROY, avocat au Barreau de Paris

c/

Mme Sophie MARTIN
Demanderesse


PLAISE AU TRIBUNAL

I. RAPPEL DES FAITS

1. M. Jean BERNARD a été propriétaire de l'appartement situé au
12 rue des Lilas, 75011 Paris, pendant une durée de 12 ans, de 2011 à 2023.

2. Durant cette période, M. BERNARD a toujours entretenu le bien avec soin
et n'a jamais constaté d'infiltrations d'eau significatives dans l'appartement.

3. Les travaux de peinture réalisés en janvier 2023 s'inscrivaient dans
le cadre d'un rafraîchissement esthétique normal en vue de la vente, pratique
courante et légitime dans le cadre d'une transaction immobilière.

4. L'acte de vente du 15 mars 2023 a été signé après que l'acquéreur
a eu tout loisir de visiter le bien à deux reprises et de faire réaliser
les diagnostics qu'elle estimait nécessaires.

5. M. BERNARD conteste formellement avoir eu connaissance d'un quelconque
défaut d'étanchéité de la toiture-terrasse, laquelle relève des parties
communes de la copropriété et non de sa responsabilité individuelle.


II. PRETENTIONS

M. BERNARD demande au Tribunal de bien vouloir :

- A titre principal, DEBOUTER Mme MARTIN de l'ensemble de ses demandes ;

- A titre subsidiaire, REDUIRE le montant des dommages et intérêts à
  de plus justes proportions en tenant compte de la vétusté de l'ouvrage
  et de la part imputable au syndicat des copropriétaires ;

- CONDAMNER Mme MARTIN au paiement de la somme de 8 000 euros à titre
  de dommages et intérêts pour procédure abusive ;

- CONDAMNER Mme MARTIN aux entiers dépens et au paiement de 4 000 euros
  au titre de l'article 700 du Code de procédure civile.


III. MOYENS

A. Sur l'absence de vice caché

Les conditions de la garantie des vices cachés ne sont pas réunies :

- Le défaut d'étanchéité de la toiture-terrasse est un désordre affectant
  les parties communes de la copropriété, et non un vice propre au lot vendu ;
- L'acquéreur avait la possibilité de consulter les procès-verbaux
  d'assemblée générale qui mentionnaient des discussions sur l'entretien
  de la toiture, ce qui rendait le vice apparent avec un minimum de diligence ;
- Le rapport d'expertise de Mme MARTIN est un rapport unilatéral, non
  contradictoire, dont la valeur probante est contestée.

B. Sur la clause d'exclusion de garantie

L'acte de vente contient une clause d'exclusion de la garantie des vices
cachés en son article 8, stipulant :
"L'acquéreur prend le bien dans l'état où il se trouve au jour de l'entrée
en jouissance, sans recours contre le vendeur pour quelque cause que ce soit,
notamment en raison des vices cachés."

Cette clause, valable entre non-professionnels de l'immobilier, fait
obstacle à toute action sur le fondement des articles 1641 et suivants
du Code civil (Cass. 3e civ., 14 mars 2012, n° 11-10.861).

C. Sur l'absence de mauvaise foi

M. BERNARD conteste toute mauvaise foi :
- Les réparations anciennes constatées par l'expert sont des travaux
  d'entretien courants qui ne démontrent pas la connaissance d'un vice ;
- La peinture récente relève d'une démarche normale de mise en valeur
  du bien, non d'une volonté de dissimulation ;
- M. BERNARD n'est pas un professionnel de l'immobilier et n'avait
  aucune compétence technique pour diagnostiquer un défaut d'étanchéité
  de la toiture-terrasse.

En l'absence de preuve de la mauvaise foi du vendeur, la clause
d'exclusion de garantie doit recevoir plein effet.

D. Sur la demande reconventionnelle

La procédure initiée par Mme MARTIN est abusive en ce qu'elle :
- Impute au vendeur un désordre relevant de la copropriété ;
- Se fonde sur un rapport d'expertise non contradictoire ;
- Formule des demandes disproportionnées.

PAR CES MOTIFS, il est demandé au Tribunal de rejeter l'ensemble
des demandes de Mme MARTIN et de faire droit aux demandes reconventionnelles.

Fait à Paris, le 28 février 2024
Maître François LEROY"""


if __name__ == "__main__":
    create_pdf("conclusions-demandeur.pdf", "CONCLUSIONS EN DEMANDE — Mme MARTIN", DEMANDEUR)
    create_pdf("conclusions-defendeur.pdf", "CONCLUSIONS EN DÉFENSE — M. BERNARD", DEFENDEUR)
    print("PDF de test générés avec succès.")
