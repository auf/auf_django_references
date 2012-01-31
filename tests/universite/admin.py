from auf.django.references.forms import EtablissementForm
from django import forms
from django.contrib import admin

from tests.universite.models import Universite

class UniversiteForm(EtablissementForm):

    class Meta(EtablissementForm.Meta):
        model = Universite
        fields = ('nom', 'pays', 'region', 'ville', 'membre', 'membre_adhesion_date', 'recteur', 'ref')

class UniversiteAdmin(admin.ModelAdmin):
    form = UniversiteForm

admin.site.register(Universite, UniversiteAdmin)
