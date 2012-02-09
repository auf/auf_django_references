# -=- encoding: utf-8 -=-

from django.db import models

from auf.django.references.managedref import models as managedref


### Proxies vers les modèles dans managedref

class Pays(managedref.Pays):

    class Meta:
        proxy = True
        managed = False


class Region(managedref.Region):

    class Meta:
        proxy = True
        managed = False


class Bureau(managedref.Bureau):

    class Meta:
        proxy = True
        managed = False


class Implantation(managedref.Implantation):

    class Meta:
        proxy = True
        managed = False


class Etablissement(managedref.Etablissement):

    class Meta:
        proxy = True
        managed = False


class Employe(managedref.Employe):

    class Meta:
        proxy = True
        managed = False


class Authentification(managedref.Authentification):

    class Meta:
        proxy = True
        managed = False


class Service(managedref.Service):

    class Meta:
        proxy = True
        managed = False


class PosteType(managedref.PosteType):

    class Meta:
        proxy = True
        managed = False


class GroupeArh(managedref.GroupeArh):

    class Meta:
        proxy = True
        managed = False


class GroupeDirRegion(managedref.GroupeDirRegion):

    class Meta:
        proxy = True
        managed = False


class GroupeAdmRegion(managedref.GroupeAdmRegion):

    class Meta:
        proxy = True
        managed = False


class GroupeRespImplantation(managedref.GroupeRespImplantation):

    class Meta:
        proxy = True
        managed = False


class GroupeDirProgramme(managedref.GroupeDirProgramme):

    class Meta:
        proxy = True
        managed = False


class GroupeDirDelegProgrammeReg(managedref.GroupeDirDelegProgrammeReg):

    class Meta:
        proxy = True
        managed = False


class GroupeComptable(managedref.GroupeComptable):

    class Meta:
        proxy = True
        managed = False


class GroupeComptableRegional(managedref.GroupeComptableRegional):

    class Meta:
        proxy = True
        managed = False


class GroupeComptableLocal(managedref.GroupeComptableLocal):

    class Meta:
        proxy = True
        managed = False


class Discipline(managedref.Discipline):

    class Meta:
        proxy = True
        managed = False


class Programme(managedref.Programme):

    class Meta:
        proxy = True
        managed = False


class Projet(managedref.Projet):

    class Meta:
        proxy = True
        managed = False


class ProjetComposante(managedref.ProjetComposante):

    class Meta:
        proxy = True
        managed = False


class UniteProjet(managedref.UniteProjet):

    class Meta:
        proxy = True
        managed = False


class ObjectifSpecifique(managedref.ObjectifSpecifique):

    class Meta:
        proxy = True
        managed = False


class ObjectifStrategique(managedref.ObjectifStrategique):

    class Meta:
        proxy = True
        managed = False


class Thematique(managedref.Thematique):

    class Meta:
        proxy = True
        managed = False


class ProjetUp(managedref.ProjetUp):

    class Meta:
        proxy = True
        managed = False


class Poste(managedref.Poste):

    class Meta:
        proxy = True
        managed = False


class ProjetPoste(managedref.ProjetPoste):

    class Meta:
        proxy = True
        managed = False


### Modèles abstraits

class EtablissementBase(managedref.EtablissementBase):
    ref = models.OneToOneField(Etablissement, blank=True, null=True,
                               related_name='%(app_label)s_%(class)s')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.ref and not self.pk:
            # Nouvel établissement faisant référence à un établissement dans
            # les références. On copie tous les champs.
            for f in self.ref._meta.fields:
                if f.attname != 'id':
                    setattr(self, f.attname, getattr(self.ref, f.attname))
        super(EtablissementBase, self).save(*args, **kwargs)
