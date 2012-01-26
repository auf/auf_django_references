from django.db import models

from auf.django.references import models as ref

class Universite(ref.EtablissementBase):
    recteur = models.CharField(max_length=100)
