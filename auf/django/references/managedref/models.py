# encoding: utf-8

from django.db import models


class Region(models.Model):
    """Région (donnée de référence, source: referentiels_spip).
    Une région est une subdivision géographique du monde pour la gestion de l'AUF.
    """
    code = models.CharField(max_length=255, unique=True)
    nom = models.CharField(max_length=255, db_index=True)
    implantation_bureau = models.ForeignKey('Implantation',
                                            db_column='implantation_bureau',
                                            related_name='gere_region', null=True, blank=True)
    # meta
    actif = models.BooleanField()

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
    implantation = models.ForeignKey('Implantation', db_column='implantation')
    region = models.ForeignKey('Region', db_column='region')
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
    bureau_rattachement = models.ForeignKey('Implantation', db_column='bureau_rattachement')
    region = models.ForeignKey('Region', db_column='region')
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
    adresse_postale_pays = models.ForeignKey('Pays', to_field='code', db_column='adresse_postale_pays', related_name='impl_adresse_postale')
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
    adresse_physique_pays = models.ForeignKey('Pays', to_field='code', db_column='adresse_physique_pays', related_name='impl_adresse_physique')
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
    region = models.ForeignKey('Region', db_column='region')
    code_bureau = models.ForeignKey('Bureau', to_field='code',
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

    def get_query_set(self):
        qs = super(EtablissementManager, self).get_query_set()
        return qs.select_related('pays')


class EtablissementBase(models.Model):
    """
    Établissement (donnée de référence, source: GDE).
    Un établissement peut être une université, un centre de recherche, un réseau d'établissement...
    Un établissement peut être membre de l'AUF ou non.
    """
    nom = models.CharField(max_length=255)
    pays = models.ForeignKey('Pays', to_field='code', db_column='pays',
                             related_name='+')
    region = models.ForeignKey('Region', db_column='region', blank=True,
                               null=True, related_name='+')
    implantation = models.ForeignKey('Implantation',
                                     db_column='implantation',
                                     related_name='+', blank=True, null=True)
    # membership
    membre = models.BooleanField()
    membre_adhesion_date = models.DateField(null=True, blank=True)
    # responsable
    responsable_genre = models.CharField(max_length=1, blank=True)
    responsable_nom = models.CharField(max_length=255, blank=True)
    responsable_prenom = models.CharField(max_length=255, blank=True)
    # adresse
    adresse = models.CharField(max_length=255, blank=True)
    code_postal = models.CharField(max_length=20, blank=True)
    cedex = models.CharField(max_length=20, blank=True)
    ville = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=255, blank=True)
    fax = models.CharField(max_length=255, blank=True)
    url = models.URLField(verify_exists=False, max_length=255, null=True, blank=True)
    # meta
    actif = models.BooleanField()
    # manager
    objects = EtablissementManager()

    class Meta:
        abstract = True
        ordering = ['pays__nom', 'nom']

    def __unicode__(self):
        return "%s - %s (%d)" % (self.pays.nom, self.nom, self.id)


class Etablissement(EtablissementBase):

    class Meta(EtablissementBase.Meta):
        db_table = u'ref_etablissement'
