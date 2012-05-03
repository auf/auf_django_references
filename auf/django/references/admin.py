from django.contrib import admin
from auf.django.references import models as ref

admin.site.register(ref.Region)
admin.site.register(ref.Bureau)
admin.site.register(ref.Implantation)
admin.site.register(ref.Pays)
admin.site.register(ref.Etablissement)
