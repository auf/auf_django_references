Extension locale des établissements de référence
================================================

Il arrive qu'on veuille dresser une liste d'établissements qui contienne à la
fois des établissements provenant des données de référence et d'autres
établissements dont les données seront conservées dans une table locale à
l'application. Le module ``auf.django.references`` fournit un mécanisme pour créer
un modèle pour une liste d'établissements qui feront, pour certains, référence
aux données de référence.  Cette référence permettra leur mise à jour
périodique.

Pour créer le modèle, il suffit de créer une sous-classe de
``auf.django.references.models.EtablissementBase``, comme ceci::

    from auf.django.references import models as ref
    from django.db import models

    class Universite(ref.EtablissementBase):
        recteur = models.CharField(max_length=200)

``EtablissementBase`` est un modèle abstrait. Les modèles qui en héritent
auront tous les champs qu'un établissement de référence contient, plus un champ
``ref`` qui sera le pointeur optionnel vers l'établissement de référence. Dans
l'exemple ci-haut, on définit en plus un champ ``recteur``. Ce champ s'ajoute au
modèle, comme on peut s'y attendre.

On peut créer des instances de ce nouveau modèle de deux façons différentes.
Pour créer une instance qui fait référence à un établissement de référence, on
fera, par exemple::

    udem_ref = ref.Etablissement.objects.get(nom='Université de Montréal')
    udem = Universite.objects.create(ref=udem_ref, recteur='Alice')

À la création, les données de ``udem_ref`` seront copiées dans ``udem``. Elles
seront aussi mises à jour à chaque sauvegarde de l'instance.

Pour créer une instance qui ne fait pas référence à un établissement de
référence, on omettra le champ ``ref``::

    uqam = Universite.objects.create(nom='UQAM', pays_id='CA', recteur='Benoît')

Mise à jour des établissements avec les données de référence
------------------------------------------------------------

Comme on l'a remarqué plus haut, les données des établissements de référence
sont copiées dans les établissements locaux qui y font référence lors de leur
création et de leur sauvegarde. Pour s'assurer que d'éventuels changements
aux données de référence soient propagés aux tables locales, il faut exécuter
périodiquement la commande Django ``sync_references``::

    bin/django sync_references

Formulaire de création et d'édition des établissements
------------------------------------------------------

Le module ``auf.django.references`` fournit un formulaire d'édition des
établissements qui offre en auto-complétion les établissements de référence
lorsqu'on entre le nom de l'établissement. Si un établissement de référence est
sélectionné, le champ ``ref`` est renseigné et les champs propres aux
établissements de référence sont pré-remplis et désactivés.

Le formulaire ``auf.django.references.forms.EtablissementForm`` est conçu pour
être sous-classé. En voici un exemple d'utilisation::

    from auf.django.references.forms import EtablissementForm

    class UniversiteForm(EtablissementForm):

        class Meta(EtablissementForm.Meta):
            model = Universite
            fields = ('pays', 'nom', 'region', 'ville', 'recteur', 'ref')

Il importe d'inclure le champ ``ref`` dans le formulaire pour que la mécanique
fonctionne. Le champ n'apparaîtra pas sur la page, mais sera utilisé pour
communiquer la référence au besoin.

Pour que l'auto-complétion fonctionne, il faut aussi inclure les url patterns
d'``auf.django.references``. Dans votre ``urls.py``::

    urlpatterns = patterns(
        ...
        (r'^references/', include('auf.django.references.urls')),
        ...
    )

On peut utiliser ce formulaire dans l'admin Django. Il suffit de le spécifier
dans la configuration de l'admin::

    from django.contrib import admin

    class UniversiteAdmin(admin.ModelAdmin):
        form = UniversiteForm

    admin.register(Universite, UniversiteForm)
