from django.contrib import admin

from tests.universite.forms import UniversiteForm
from tests.universite.models import Universite

class UniversiteAdmin(admin.ModelAdmin):
    form = UniversiteForm

admin.site.register(Universite, UniversiteAdmin)
