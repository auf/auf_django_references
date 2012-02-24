# encoding: utf-8

from django.db import models


class ActifsManager(models.Manager):

    def get_query_set(self):
        return super(ActifsManager, self).get_query_set().filter(actif=True)


class Employe(models.Model):
    """Personne en contrat d'employé (CDD ou CDI) à l'AUF
    """
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    implantation = models.ForeignKey(
        'references.Implantation',
        db_column='implantation',
        related_name='lieu_travail_theorique_de'
    )
    implantation_physique = models.ForeignKey(
        'references.Implantation',
        db_column='implantation_physique',
        related_name='lieu_travail_reel_de'
    )
    courriel = models.CharField(max_length=255, null=True, blank=True)
    genre = models.CharField(max_length=3)
    fonction = models.CharField(max_length=255, null=True, blank=True)
    telephone_poste = models.CharField(max_length=255, null=True, blank=True)
    telephone_ip = models.CharField(max_length=255, null=True, blank=True)
    responsable = models.ForeignKey(
        'references.Employe',
        db_column='responsable',
        related_name='responsable_de',
        null=True, blank=True
    )
    mandat_debut = models.DateField(null=True, blank=True)
    mandat_fin = models.DateField(null=True, blank=True)
    date_entree = models.DateField(null=True, blank=True)
    service = models.ForeignKey('references.Service', db_column='service')
    poste_type_1 =  models.ForeignKey(
        'references.PosteType',
        null=True, blank=True,
        db_column='poste_type_1',
        related_name='poste_type_1'
    )
    poste_type_2 =  models.ForeignKey(
        'references.PosteType',
        null=True, blank=True,
        db_column='poste_type_2',
        related_name='poste_type_2'
    )
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_employe'
        ordering = ['nom']

    def __unicode__(self):
        return u"%s, %s [%d]" % (self.nom, self.prenom, self.id)


class Authentification(models.Model):
    """Authentification"""
    id = models.ForeignKey('references.Employe', primary_key=True, db_column='id')
    courriel = models.CharField(max_length=255, unique=True)
    motdepasse = models.CharField(max_length=255)
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_authentification'
        ordering = ['id']

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

    def __unicode__(self):
        return "%s (%s)" % (self.nom, self.id)


class GroupeArh(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('references.Employe', db_column='employe')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_arh'


class GroupeDirRegion(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('references.Employe', db_column='employe')
    region = models.ForeignKey('references.Region', db_column='region')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_dir_region'


class GroupeAdmRegion(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('references.Employe', db_column='employe')
    region = models.ForeignKey('references.Region', db_column='region')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_adm_region'


class GroupeRespImplantation(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('references.Employe', db_column='employe')
    implantation = models.ForeignKey('references.Implantation', db_column='implantation')
    type = models.CharField(max_length=255, blank=True, null=True)
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_resp_implantation'


class GroupeDirProgramme(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('references.Employe', db_column='employe')
    service = models.ForeignKey('references.Service', db_column='service')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_dir_programme'


class GroupeDirDelegProgrammeReg(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('references.Employe', db_column='employe')
    region = models.ForeignKey('references.Region', db_column='region')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_dir_deleg_programme_reg'


class GroupeComptable(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('references.Employe', db_column='employe')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_comptable'


class GroupeComptableRegional(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('references.Employe', db_column='employe')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_comptable_regional'


class GroupeComptableLocal(models.Model):
    id = models.AutoField(primary_key=True)
    employe = models.ForeignKey('references.Employe', db_column='employe')
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_groupe_comptable_local'


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

    def __unicode__(self):
        return "%s - %s" % (self.code, self.nom)


#PROGRAMMATION QUADRIENNALLE

class Projet(models.Model):
    """Projet (donnée de référence, source: programmation-quadriennalle).
    """
    SERVICE_CHOICES = (
        ('1', "Direction de la langue et de la communication scientifique en français"),
        ('2', "Direction du développement et de la valorisation"),
        ('3', "Direction de l'innovation pédagogique et de l'économie de la connaissance"),
        ('4', "Direction du renforcement des capacités scientifiques"),
    )

    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255)
    presentation = models.TextField(null=True, blank=True)
    partenaires = models.TextField(null=True, blank=True)
    service = models.CharField(max_length=255, choices=SERVICE_CHOICES, blank=True, null=True)
    objectif_specifique = models.ForeignKey(
        'references.ObjectifSpecifique',
        blank=True, null=True,
        db_column='objectif_specifique'
    )
    implantation = models.ForeignKey('references.Implantation', null=True,
                                     blank=True, db_column='implantation')
    etablissement = models.ForeignKey('references.Etablissement', null=True,
                                      blank=True, db_column='etablissement')
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_projet'
        ordering = ['nom']

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
    projet = models.ForeignKey('references.Projet', db_column='projet')
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_projet_composante'
        ordering = ['nom']

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

    def __unicode__(self):
        return "%s - %s" % (self.code, self.nom)


class ObjectifSpecifique(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    objectif_strategique = models.ForeignKey('references.ObjectifStrategique',
                                             db_column='objectif_strategique')
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_objectif_specifique'
        ordering = ['nom']

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
    code_projet = models.ForeignKey('references.Projet', to_field='code', db_column='code_projet')
    code_poste = models.ForeignKey('references.Poste', to_field='code', db_column='code_poste')
    code_bureau = models.ForeignKey('references.Bureau', to_field='code', db_column='code_bureau')
    code_programme = models.ForeignKey('references.Programme',
                                       to_field='code',
                                       db_column='code_programme')
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_projet_poste'

    def __unicode__(self):
        return "%s" % (self.code)


class Region(models.Model):
    """Région (donnée de référence, source: referentiels_spip).
    Une région est une subdivision géographique du monde pour la gestion de l'AUF.
    """
    code = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255, db_index=True)
    implantation_bureau = models.ForeignKey('references.Implantation',
                                            db_column='implantation_bureau',
                                            related_name='gere_region', null=True, blank=True)
    # meta
    actif = models.BooleanField()

    # managers
    objects = ActifsManager()
    avec_inactifs = models.Manager()

    class Meta:
        db_table = u'ref_region'
        ordering = ['nom']
        verbose_name = u"région"
        verbose_name_plural = u"régions"

    def __unicode__(self):
        return "%s (%s)" % (self.nom, self.code)


class Bureau(models.Model):
    """Bureau (donnée de référence, source: SQI).
    Référence legacy entre la notion de région et celle d'implantation responsable des régions et du central.
    Un bureau est :
    - soit le bureau régional d'une région (implantations de type 'Bureau')
    - soit la notion unique de Service central pour les 2 implantations centrales (implantations de type 'Service central' et 'Siege').
    Ne pas confondre avec les seuls 'bureaux régionaux'.
    """
    code = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255)
    nom_court = models.CharField(max_length=255, blank=True)
    nom_long = models.CharField(max_length=255, blank=True)
    implantation = models.ForeignKey('references.Implantation', db_column='implantation')
    region = models.ForeignKey('references.Region', db_column='region')
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_bureau'
        ordering = ['nom']
        verbose_name = u"bureau"
        verbose_name_plural = u"bureaux"

    def __unicode__(self):
        return "%s (%s)" % (self.nom, self.code)


class Implantation(models.Model):
    """Implantation (donnée de référence, source: Implantus)
    Une implantation est un endroit où l'AUF est présente et offre des services spécifiques.
    Deux implantations peuvent être au même endroit physique.
    """
    nom = models.CharField(max_length=255)
    nom_court = models.CharField(max_length=255, blank=True)
    nom_long = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255)
    bureau_rattachement = models.ForeignKey('references.Implantation', db_column='bureau_rattachement')
    region = models.ForeignKey('references.Region', db_column='region')
    fuseau_horaire = models.CharField(max_length=255, blank=True)
    code_meteo = models.CharField(max_length=255, blank=True)
    # responsable
    responsable_implantation = models.IntegerField(null=True, blank=True)   # models.ForeignKey('Employe')
    # adresse postale
    adresse_postale_precision_avant = models.CharField(max_length=255, blank=True, null=True)
    adresse_postale_no = models.CharField(max_length=30, blank=True, null=True)
    adresse_postale_rue = models.CharField(max_length=255, blank=True, null=True)
    adresse_postale_bureau = models.CharField(max_length=255, blank=True, null=True)
    adresse_postale_precision = models.CharField(max_length=255, blank=True, null=True)
    adresse_postale_boite_postale = models.CharField(max_length=255, blank=True, null=True)
    adresse_postale_ville = models.CharField(max_length=255)
    adresse_postale_code_postal = models.CharField(max_length=20, blank=True, null=True)
    adresse_postale_code_postal_avant_ville = models.NullBooleanField()
    adresse_postale_region = models.CharField(max_length=255, blank=True, null=True)
    adresse_postale_pays = models.ForeignKey('references.Pays',
                                             to_field='code',
                                             db_column='adresse_postale_pays',
                                             related_name='impl_adresse_postale')
    # adresse physique
    adresse_physique_precision_avant = models.CharField(max_length=255, blank=True)
    adresse_physique_no = models.CharField(max_length=30, blank=True)
    adresse_physique_rue = models.CharField(max_length=255, blank=True)
    adresse_physique_bureau = models.CharField(max_length=255, blank=True)
    adresse_physique_precision = models.CharField(max_length=255, blank=True)
    adresse_physique_ville = models.CharField(max_length=255)
    adresse_physique_code_postal = models.CharField(max_length=30, blank=True)
    adresse_physique_code_postal_avant_ville = models.NullBooleanField()
    adresse_physique_region = models.CharField(max_length=255, blank=True)
    adresse_physique_pays = models.ForeignKey('references.Pays',
                                              to_field='code',
                                              db_column='adresse_physique_pays',
                                              related_name='impl_adresse_physique')
    # autres coordonnées
    telephone = models.CharField(max_length=255, blank=True)
    telephone_interne = models.CharField(max_length=255, blank=True)
    fax = models.CharField(max_length=255, blank=True)
    fax_interne = models.CharField(max_length=255, blank=True)
    courriel = models.EmailField(blank=True)
    courriel_interne = models.EmailField(blank=True)
    url = models.URLField(verify_exists=False, max_length=255, blank=True)
    # traitement
    statut = models.IntegerField()
    date_ouverture = models.DateField(null=True, blank=True)
    date_inauguration = models.DateField(null=True, blank=True)
    date_extension = models.DateField(null=True, blank=True)
    date_fermeture = models.DateField(null=True, blank=True)
    hebergement_etablissement = models.CharField(max_length=255, blank=True)    # models.ForeignKey('Etablissement', db_column='hebergement_etablissement')
    hebergement_convention = models.NullBooleanField()
    hebergement_convention_date = models.DateField(null=True, blank=True)
    remarque = models.TextField()
    commentaire = models.CharField(max_length=255, blank=True)
    # meta
    actif = models.BooleanField()
    modif_date = models.DateField()

    class Managers:

        class Ouvertes(models.Manager):

            def get_query_set(self):
                return super(Implantation.Managers.Ouvertes, self).get_query_set().filter(
                    actif=True, statut=1
                )

        class Actifs(models.Manager):

            def get_query_set(self):
                return super(Implantation.Managers.Actifs, self).get_query_set().filter(actif=True)

    objects = models.Manager()
    ouvertes = Managers.Ouvertes()
    actifs = Managers.Actifs()
    actives = actifs

    class Meta:
        db_table = u'ref_implantation'
        ordering = ['nom']

    def __unicode__(self):
        return "%s (%d)" % (self.nom, self.id)


class Pays(models.Model):
    """Pays (donnée de référence, source: SQI).  Liste AUF basée sur la liste ISO-3166-1.  """
    code = models.CharField(max_length=2, unique=True)
    code_iso3 = models.CharField(max_length=3, unique=True)
    nom = models.CharField(max_length=255)
    region = models.ForeignKey('references.Region', db_column='region')
    code_bureau = models.ForeignKey('references.Bureau', to_field='code',
                                    db_column='code_bureau', blank=True,
                                    null=True)
    nord_sud = models.CharField(max_length=255, blank=True, null=True)
    developpement = models.CharField(max_length=255, blank=True, null=True)
    monnaie = models.CharField(max_length=255, blank=True, null=True)
    # meta
    actif = models.BooleanField()

    class Meta:
        db_table = u'ref_pays'
        ordering = ['nom']
        verbose_name = u"pays"
        verbose_name_plural = u"pays"

    def __unicode__(self):
        return "%s (%s)" % (self.nom, self.code)


class EtablissementManager(models.Manager):

    def __init__(self, avec_inactifs=False):
        super(EtablissementManager, self).__init__()
        self.avec_inactifs=avec_inactifs

    def get_query_set(self):
        qs = super(EtablissementManager, self).get_query_set()
        if not self.avec_inactifs:
            qs = qs.filter(actif=True)
        return qs.select_related('pays')


class EtablissementBase(models.Model):
    """
    Établissement (donnée de référence, source: GDE).
    Un établissement peut être une université, un centre de recherche, un réseau d'établissement...
    Un établissement peut être membre de l'AUF ou non.
    """
    MEMBRE_STATUT_CHOICES = (
        ('T', 'Titulaire'),
        ('A', 'Associé'),
        ('C', 'Candidat'),
    )
    QUALITE_CHOICES = (
        ('ESR', "Établissement d'enseignement supérieur et de recherche"),
        ('CIR', "Centre ou institution de recherche"),
        ('RES', "Réseau"),
    )

    # Infos de base
    nom = models.CharField(max_length=255)
    pays = models.ForeignKey('references.Pays', to_field='code', db_column='pays',
                             related_name='+')
    region = models.ForeignKey('references.Region', db_column='region', blank=True,
                               null=True, related_name='+', verbose_name='région')
    implantation = models.ForeignKey('references.Implantation',
                                     db_column='implantation',
                                     related_name='+', blank=True, null=True)

    # Membership
    membre = models.BooleanField()
    membre_adhesion_date = models.DateField(null=True, blank=True,
                                            verbose_name="date d'adhésion")
    statut = models.CharField(max_length=1, choices=MEMBRE_STATUT_CHOICES,
                              blank=True, null=True)
    qualite = models.CharField(max_length=3, choices=QUALITE_CHOICES,
                               verbose_name="qualité", blank=True,
                               null=True)

    # Responsable
    responsable_genre = models.CharField(max_length=1, blank=True,
                                         verbose_name='genre')
    responsable_nom = models.CharField(max_length=255, blank=True,
                                       verbose_name='nom')
    responsable_prenom = models.CharField(max_length=255, blank=True,
                                          verbose_name='prénom')

    # Adresse
    adresse = models.CharField(max_length=255, blank=True)
    code_postal = models.CharField(max_length=20, blank=True,
                                   verbose_name='code postal')
    cedex = models.CharField(max_length=20, blank=True, verbose_name='CEDEX')
    ville = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=255, blank=True,
                                 verbose_name='téléphone')
    fax = models.CharField(max_length=255, blank=True)
    url = models.URLField(verify_exists=False, max_length=255, null=True,
                          blank=True, verbose_name='URL')

    # Meta-données
    actif = models.BooleanField(default=True)
    date_modification = models.DateField(verbose_name='date de modification',
                                         blank=True, null=True)
    commentaire = models.TextField(blank=True)

    # Manager
    objects = EtablissementManager()
    avec_inactifs = EtablissementManager(avec_inactifs=True)

    class Meta:
        abstract = True
        ordering = ['pays__nom', 'nom']

    def __unicode__(self):
        return "%s - %s" % (self.pays.nom, self.nom)


class Etablissement(EtablissementBase):

    class Meta(EtablissementBase.Meta):
        db_table = u'ref_etablissement'
