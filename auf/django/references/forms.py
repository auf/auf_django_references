from django import forms

from auf.django.references import models as ref

class EtablissementForm(forms.ModelForm):
    nom = forms.CharField(widget=forms.TextInput(attrs={'class': 'etablissement-autocomplete'}))

    class Meta:
        model = ref.EtablissementBase

    class Media:
        css = {
            'screen': ('references/jquery-ui.css',)
        }
        js = (
            'references/jquery.min.js',
            'references/jquery-ui.min.js',
            'references/etablissement-form.js',
        )

