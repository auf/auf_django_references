from __future__ import absolute_import

from django.contrib import admin

from tests.universite.models import Universite
from tests.universite.forms import UniversiteForm

class UniversiteAdmin(admin.ModelAdmin):
    form = UniversiteForm

admin.site.register(Universite, UniversiteAdmin)
