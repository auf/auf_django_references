from __future__ import absolute_import

from auf.django.references.forms import EtablissementForm

from tests.universite.models import Universite

class UniversiteForm(EtablissementForm):

    class Meta(EtablissementForm.Meta):
        model = Universite
        fields = ('nom', 'pays', 'region', 'ville', 'membre', 'membre_adhesion_date', 'recteur', 'ref')
