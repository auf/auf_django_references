from django.core.urlresolvers import reverse
from django.db import models

from auf.django.references import models as ref

class Universite(ref.EtablissementBase):
    recteur = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('universite_update', kwargs={'pk': self.pk})
