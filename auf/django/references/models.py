# -=- encoding: utf-8 -=-

from django.db import models

from auf.django.references.managedref import models as managedref

class Employe(models.Model):
    """Personne en contrat d'employé (CDD ou CDI) à l'AUF
    """
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    implantation = models.ForeignKey(to='Implantation', db_column='implantation', related_name='lieu_travail_theorique_de')    # SGRH
    implantation_physique = models.ForeignKey(to='Implantation', db_column='implantation_physique', related_name='lieu_travail_reel_de')
    courriel = models.CharField(max_length=255, null=True, blank=True)
    genre = models.CharField(max_length=3)
    fonction = models.CharField(max_length=255, null=True, blank=True)
    telephone_poste = models.CharField(max_length=255, null=True, blank=True)
    telephone_ip = models.CharField(max_length=255, null=True, blank=True)
    responsable = models.ForeignKey(to='Employe', db_column='responsable', related_name='responsable_de', null=True, blank=True)
    mandat_debut = models.DateField(null=True, blank=True)
    mandat_fin = models.DateField(null=True, blank=True)
    date_entree = models.DateField(null=True, blank=True)
    service = models.ForeignKey('Service', db_column='service')
    poste_type_1 =  models.ForeignKey('PosteType', null=True, blank=True, db_column='poste_type_1', related_name='poste_type_1')
    poste_type_2 =  models.ForeignKey('PosteType', null=True, blank=True, db_column='poste_type_2', related_name='poste_type_2')
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_employe'
        ordering = ['nom']
        managed = False

    def __unicode__(self):
        return u"%s, %s [%d]" % (self.nom, self.prenom, self.id)

class Authentification(models.Model):
    """Authentification"""
    id = models.ForeignKey('Employe', primary_key=True, db_column='id')
    courriel = models.CharField(max_length=255, unique=True)
    motdepasse = models.CharField(max_length=255)
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_authentification'
        ordering = ['id']
        managed = False

    def __unicode__(self):
        return u"%s [%d]" % (self.courriel, self.id)

class Service(models.Model):
    """Services (donnée de référence, source: SGRH).
    """
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_service'
        ordering = ['nom']
        managed = False

    def __unicode__(self):
        return "%s (%s)" % (self.nom, self.id)

class PosteType(models.Model):
    """Postes types (donnée de référence, source: SGRH).
    """
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_poste_type'
        managed = False

    def __unicode__(self):
        return "%s (%s)" % (self.nom, self.id)

class GroupeArh(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('Employe', db_column='employe')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_arh'
        managed = False

class GroupeDirRegion(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('Employe', db_column='employe')
    region = models.ForeignKey('Region', db_column='region')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_dir_region'
        managed = False

class GroupeAdmRegion(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('Employe', db_column='employe')
    region = models.ForeignKey('Region', db_column='region')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_adm_region'
        managed = False

class GroupeRespImplantation(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('Employe', db_column='employe')
    implantation = models.ForeignKey('Implantation', db_column='implantation')
    type = models.CharField(max_length=255, blank=True, null=True)
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_resp_implantation'
        managed = False

class GroupeDirProgramme(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('Employe', db_column='employe')
    service = models.ForeignKey('Service', db_column='service')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_dir_programme'
        managed = False

class GroupeDirDelegProgrammeReg(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('Employe', db_column='employe')
    region = models.ForeignKey('Region', db_column='region')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_dir_deleg_programme_reg'
        managed = False

class GroupeComptable(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('Employe', db_column='employe')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_comptable'
        managed = False

class GroupeComptableRegional(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('Employe', db_column='employe')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_comptable_regional'
        managed = False

class GroupeComptableLocal(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('Employe', db_column='employe')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_comptable_local'
        managed = False

class Discipline(models.Model):
    """ ATTENTION: DÉSUET
    Discipline (donnée de référence, source: SQI).
    Une discipline est une catégorie de savoirs scientifiques.
    Le conseil scientifique fixe la liste des disciplines.
    """

    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255)
    nom_long = models.CharField(max_length=255, blank=True)
    nom_court = models.CharField(max_length=255, blank=True)
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_discipline'
        ordering = ['nom']
        managed = False

    def __unicode__(self):
        return "%s - %s" % (self.code, self.nom)

class Programme(models.Model):
    """ ATTENTION: DÉSUET
    Programme (donnée de référence, source: SQI).
    Structure interne par laquelle l'AUF exécute ses projets et activités, dispense ses produits et ses services.
    """

    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255)
    nom_long = models.CharField(max_length=255, blank=True)
    nom_court = models.CharField(max_length=255, blank=True)
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_programme'
        managed = False

    def __unicode__(self):
        return "%s - %s" % (self.code, self.nom)

#PROGRAMMATION QUADRIENNALLE

SERVICE_CHOICES = (
        ('1', "Direction de la langue et de la communication scientifique en français"),
        ('2', "Direction du développement et de la valorisation"),
        ('3', "Direction de l'innovation pédagogique et de l'économie de la connaissance"),
        ('4', "Direction du renforcement des capacités scientifiques"),
        )

class Projet(models.Model):
    """Projet (donnée de référence, source: programmation-quadriennalle).
    """

    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255)
    presentation = models.TextField(null=True, blank=True)
    partenaires = models.TextField(null=True, blank=True)
    service = models.CharField(max_length=255, choices=SERVICE_CHOICES, blank=True, null=True)
    objectif_specifique = models.ForeignKey('ObjectifSpecifique', blank=True, null=True, db_column='objectif_specifique')
    implantation = models.ForeignKey('Implantation', null=True, blank=True, db_column='implantation')
    etablissement = models.ForeignKey('Etablissement', null=True, blank=True, db_column='etablissement')
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_projet'
        ordering = ['nom']
        managed = False

    def __unicode__(self):
        return "%s - %s" % (self.code, self.nom)

class ProjetComposante(models.Model):
    """Composantes des projets (source: programmation-quadriennalle)
    """
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=10)
    nom = models.CharField(max_length=255)
    nom_court = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    projet = models.ForeignKey('Projet', db_column='projet')
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_projet_composante'
        ordering = ['nom']
        managed = False

    def __unicode__(self):
        return "%s - %s" % (self.code, self.nom)

class UniteProjet(models.Model):
    """Unités de projet (source: programmation-quadriennalle)
    """
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)
    nom = models.CharField(max_length=255)
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_unite_projet'
        ordering = ['nom']
        managed = False

    def __unicode__(self):
        return "%s - %s" % (self.code, self.nom)

class ObjectifSpecifique(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    objectif_strategique = models.ForeignKey('ObjectifStrategique', db_column='objectif_strategique')
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_objectif_specifique'
        ordering = ['nom']
        managed = False

    def __unicode__(self):
        return "%s - %s" % (self.id, self.nom)

class ObjectifStrategique(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_objectif_strategique'
        ordering = ['nom']
        managed = False

    def __unicode__(self):
        return "%s - %s" % (self.id, self.nom)

class Thematique(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_thematique'
        ordering = ['nom']
        managed = False

    def __unicode__(self):
        return "%s - %s" % (self.id, self.nom)

class ProjetUp(models.Model):
    """Projet-unité de projet (source: coda)
       => codes budgétaires
    """
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255)
    nom_court = models.CharField(max_length=255, blank=True)
    # meta
    actif = models.BooleanField()

    class Meta:
        managed = False

class Poste(models.Model):
    """ ATTENTION: DÉSUET
    Poste (donnée de référence, source: CODA).
    Un poste est une catégorie destinée à venir raffiner un projet.
    """

    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True)
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_poste'
        managed = False

    def __unicode__(self):
        return "%s - %s (%s)" % (self.code, self.nom, self.type)

class ProjetPoste(models.Model):
    """ ATTENTION: DÉSUET
    Projet-poste (donnée de référence, source: CODA).
    Un projet-poste consiste en une raffinement d'un projet par un poste (budgétaire).
    Subdivision utile pour le suivi budgétaire et comptable.
    """

    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255, unique=True)
    code_projet = models.ForeignKey('Projet', to_field='code', db_column='code_projet')
    code_poste = models.ForeignKey('Poste', to_field='code', db_column='code_poste')
    code_bureau = models.ForeignKey('Bureau', to_field='code', db_column='code_bureau')
    code_programme = models.ForeignKey('Programme', to_field='code', db_column='code_programme')
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_projet_poste'
        managed = False

    def __unicode__(self):
        return "%s" % (self.code)

### Proxies

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
