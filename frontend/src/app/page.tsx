import { CallOut } from "@codegouvfr/react-dsfr/CallOut";
import { Button } from "@codegouvfr/react-dsfr/Button";

export default function HomePage() {
  return (
    <div className="fr-grid-row fr-grid-row--center">
      <div className="fr-col-12 fr-col-md-8">
        <h1>Mon Assistant Civil</h1>
        <CallOut
          iconId="fr-icon-scales-3-line"
          title="Analysez vos conclusions juridiques"
          titleAs="h2"
        >
          Cet outil expérimental utilise l&apos;intelligence artificielle pour
          analyser et comparer les conclusions des parties dans une affaire
          civile. Importez les conclusions du demandeur et du défendeur pour
          obtenir une analyse structurée : faits, prétentions, moyens,
          résumés et rapport comparatif.
        </CallOut>

        <div className="fr-mt-4w">
          <h3>Comment ça marche ?</h3>
          <div className="fr-grid-row fr-grid-row--gutters fr-mt-2w">
            <div className="fr-col-12 fr-col-md-4">
              <div className="fr-tile fr-tile--horizontal">
                <div className="fr-tile__body">
                  <h4 className="fr-tile__title">1. Importez</h4>
                  <p className="fr-tile__detail">
                    Déposez les conclusions du demandeur et du défendeur au
                    format PDF.
                  </p>
                </div>
              </div>
            </div>
            <div className="fr-col-12 fr-col-md-4">
              <div className="fr-tile fr-tile--horizontal">
                <div className="fr-tile__body">
                  <h4 className="fr-tile__title">2. Analysez</h4>
                  <p className="fr-tile__detail">
                    L&apos;IA extrait et structure les informations juridiques
                    clés.
                  </p>
                </div>
              </div>
            </div>
            <div className="fr-col-12 fr-col-md-4">
              <div className="fr-tile fr-tile--horizontal">
                <div className="fr-tile__body">
                  <h4 className="fr-tile__title">3. Comparez</h4>
                  <p className="fr-tile__detail">
                    Obtenez un rapport des convergences et divergences entre les
                    parties.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="fr-mt-4w" style={{ textAlign: "center" }}>
          <Button
            size="large"
            linkProps={{ href: "/analyse" }}
            iconId="fr-icon-arrow-right-line"
            iconPosition="right"
          >
            Commencer l&apos;analyse
          </Button>
        </div>
      </div>
    </div>
  );
}
