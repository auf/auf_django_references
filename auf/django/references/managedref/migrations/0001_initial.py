# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Employe'
        db.create_table(u'ref_employe', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('implantation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lieu_travail_theorique_de', db_column='implantation', to=orm['managedref.Implantation'])),
            ('implantation_physique', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lieu_travail_reel_de', db_column='implantation_physique', to=orm['managedref.Implantation'])),
            ('courriel', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('fonction', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('telephone_poste', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('telephone_ip', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('responsable', self.gf('django.db.models.fields.related.ForeignKey')(related_name='responsable_de', blank=True, null=True, db_column='responsable', to=orm['managedref.Employe'])),
            ('mandat_debut', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('mandat_fin', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_entree', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Service'], db_column='service')),
            ('poste_type_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poste_type_1', blank=True, null=True, db_column='poste_type_1', to=orm['managedref.PosteType'])),
            ('poste_type_2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poste_type_2', blank=True, null=True, db_column='poste_type_2', to=orm['managedref.PosteType'])),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['Employe'])

        # Adding model 'Authentification'
        db.create_table(u'ref_authentification', (
            ('id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Employe'], primary_key=True, db_column='id')),
            ('courriel', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
            ('motdepasse', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['Authentification'])

        # Adding model 'Service'
        db.create_table(u'ref_service', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['Service'])

        # Adding model 'PosteType'
        db.create_table(u'ref_poste_type', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['PosteType'])

        # Adding model 'GroupeArh'
        db.create_table(u'ref_groupe_arh', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Employe'], db_column='employe')),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['GroupeArh'])

        # Adding model 'GroupeDirRegion'
        db.create_table(u'ref_groupe_dir_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Employe'], db_column='employe')),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Region'], db_column='region')),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['GroupeDirRegion'])

        # Adding model 'GroupeAdmRegion'
        db.create_table(u'ref_groupe_adm_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Employe'], db_column='employe')),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Region'], db_column='region')),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['GroupeAdmRegion'])

        # Adding model 'GroupeRespImplantation'
        db.create_table(u'ref_groupe_resp_implantation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Employe'], db_column='employe')),
            ('implantation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Implantation'], db_column='implantation')),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['GroupeRespImplantation'])

        # Adding model 'GroupeDirProgramme'
        db.create_table(u'ref_groupe_dir_programme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Employe'], db_column='employe')),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Service'], db_column='service')),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['GroupeDirProgramme'])

        # Adding model 'GroupeDirDelegProgrammeReg'
        db.create_table(u'ref_groupe_dir_deleg_programme_reg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Employe'], db_column='employe')),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Region'], db_column='region')),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['GroupeDirDelegProgrammeReg'])

        # Adding model 'GroupeComptable'
        db.create_table(u'ref_groupe_comptable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Employe'], db_column='employe')),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['GroupeComptable'])

        # Adding model 'GroupeComptableRegional'
        db.create_table(u'ref_groupe_comptable_regional', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Employe'], db_column='employe')),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['GroupeComptableRegional'])

        # Adding model 'GroupeComptableLocal'
        db.create_table(u'ref_groupe_comptable_local', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Employe'], db_column='employe')),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['GroupeComptableLocal'])

        # Adding model 'Discipline'
        db.create_table(u'ref_discipline', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nom_long', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('nom_court', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['Discipline'])

        # Adding model 'Programme'
        db.create_table(u'ref_programme', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nom_long', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('nom_court', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['Programme'])

        # Adding model 'Projet'
        db.create_table(u'ref_projet', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('presentation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('partenaires', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('service', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('objectif_specifique', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.ObjectifSpecifique'], null=True, db_column='objectif_specifique', blank=True)),
            ('implantation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Implantation'], null=True, db_column='implantation', blank=True)),
            ('etablissement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Etablissement'], null=True, db_column='etablissement', blank=True)),
            ('date_debut', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_fin', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['Projet'])

        # Adding model 'ProjetComposante'
        db.create_table(u'ref_projet_composante', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nom_court', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('projet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Projet'], db_column='projet')),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['ProjetComposante'])

        # Adding model 'UniteProjet'
        db.create_table(u'ref_unite_projet', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10, unique=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['UniteProjet'])

        # Adding model 'ObjectifSpecifique'
        db.create_table(u'ref_objectif_specifique', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('objectif_strategique', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.ObjectifStrategique'], db_column='objectif_strategique')),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['ObjectifSpecifique'])

        # Adding model 'ObjectifStrategique'
        db.create_table(u'ref_objectif_strategique', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['ObjectifStrategique'])

        # Adding model 'Thematique'
        db.create_table(u'ref_thematique', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['Thematique'])

        # Adding model 'ProjetUp'
        db.create_table('managedref_projetup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nom_court', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['ProjetUp'])

        # Adding model 'Poste'
        db.create_table(u'ref_poste', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['Poste'])

        # Adding model 'ProjetPoste'
        db.create_table(u'ref_projet_poste', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
            ('code_projet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Projet'], to_field='code', db_column='code_projet')),
            ('code_poste', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Poste'], to_field='code', db_column='code_poste')),
            ('code_bureau', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Bureau'], to_field='code', db_column='code_bureau')),
            ('code_programme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Programme'], to_field='code', db_column='code_programme')),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['ProjetPoste'])

        # Adding model 'Region'
        db.create_table(u'ref_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('implantation_bureau', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gere_region', blank=True, null=True, db_column='implantation_bureau', to=orm['managedref.Implantation'])),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['Region'])

        # Adding model 'Bureau'
        db.create_table(u'ref_bureau', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nom_court', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('nom_long', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('implantation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Implantation'], db_column='implantation')),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Region'], db_column='region')),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['Bureau'])

        # Adding model 'Implantation'
        db.create_table(u'ref_implantation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nom_court', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('nom_long', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('bureau_rattachement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Implantation'], db_column='bureau_rattachement')),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Region'], db_column='region')),
            ('fuseau_horaire', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('code_meteo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('responsable_implantation', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('adresse_postale_precision_avant', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('adresse_postale_no', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('adresse_postale_rue', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('adresse_postale_bureau', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('adresse_postale_precision', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('adresse_postale_boite_postale', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('adresse_postale_ville', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('adresse_postale_code_postal', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('adresse_postale_code_postal_avant_ville', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('adresse_postale_region', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('adresse_postale_pays', self.gf('django.db.models.fields.related.ForeignKey')(related_name='impl_adresse_postale', to_field='code', db_column='adresse_postale_pays', to=orm['managedref.Pays'])),
            ('adresse_physique_precision_avant', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('adresse_physique_no', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('adresse_physique_rue', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('adresse_physique_bureau', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('adresse_physique_precision', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('adresse_physique_ville', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('adresse_physique_code_postal', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('adresse_physique_code_postal_avant_ville', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('adresse_physique_region', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('adresse_physique_pays', self.gf('django.db.models.fields.related.ForeignKey')(related_name='impl_adresse_physique', to_field='code', db_column='adresse_physique_pays', to=orm['managedref.Pays'])),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('telephone_interne', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('fax_interne', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('courriel', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('courriel_interne', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('statut', self.gf('django.db.models.fields.IntegerField')()),
            ('date_ouverture', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_inauguration', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_extension', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_fermeture', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('hebergement_etablissement', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('hebergement_convention', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('hebergement_convention_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('remarque', self.gf('django.db.models.fields.TextField')()),
            ('commentaire', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('modif_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('managedref', ['Implantation'])

        # Adding model 'Pays'
        db.create_table(u'ref_pays', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2, unique=True)),
            ('code_iso3', self.gf('django.db.models.fields.CharField')(max_length=3, unique=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Region'], db_column='region')),
            ('code_bureau', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['managedref.Bureau'], to_field='code', null=True, db_column='code_bureau', blank=True)),
            ('nord_sud', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('developpement', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('monnaie', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['Pays'])

        # Adding model 'Etablissement'
        db.create_table(u'ref_etablissement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pays', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to_field='code', db_column='pays', to=orm['managedref.Pays'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', blank=True, null=True, db_column='region', to=orm['managedref.Region'])),
            ('implantation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', blank=True, null=True, db_column='implantation', to=orm['managedref.Implantation'])),
            ('membre', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('membre_adhesion_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('responsable_genre', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('responsable_nom', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('responsable_prenom', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('adresse', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('code_postal', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('cedex', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('managedref', ['Etablissement'])


    def backwards(self, orm):
        
        # Deleting model 'Employe'
        db.delete_table(u'ref_employe')

        # Deleting model 'Authentification'
        db.delete_table(u'ref_authentification')

        # Deleting model 'Service'
        db.delete_table(u'ref_service')

        # Deleting model 'PosteType'
        db.delete_table(u'ref_poste_type')

        # Deleting model 'GroupeArh'
        db.delete_table(u'ref_groupe_arh')

        # Deleting model 'GroupeDirRegion'
        db.delete_table(u'ref_groupe_dir_region')

        # Deleting model 'GroupeAdmRegion'
        db.delete_table(u'ref_groupe_adm_region')

        # Deleting model 'GroupeRespImplantation'
        db.delete_table(u'ref_groupe_resp_implantation')

        # Deleting model 'GroupeDirProgramme'
        db.delete_table(u'ref_groupe_dir_programme')

        # Deleting model 'GroupeDirDelegProgrammeReg'
        db.delete_table(u'ref_groupe_dir_deleg_programme_reg')

        # Deleting model 'GroupeComptable'
        db.delete_table(u'ref_groupe_comptable')

        # Deleting model 'GroupeComptableRegional'
        db.delete_table(u'ref_groupe_comptable_regional')

        # Deleting model 'GroupeComptableLocal'
        db.delete_table(u'ref_groupe_comptable_local')

        # Deleting model 'Discipline'
        db.delete_table(u'ref_discipline')

        # Deleting model 'Programme'
        db.delete_table(u'ref_programme')

        # Deleting model 'Projet'
        db.delete_table(u'ref_projet')

        # Deleting model 'ProjetComposante'
        db.delete_table(u'ref_projet_composante')

        # Deleting model 'UniteProjet'
        db.delete_table(u'ref_unite_projet')

        # Deleting model 'ObjectifSpecifique'
        db.delete_table(u'ref_objectif_specifique')

        # Deleting model 'ObjectifStrategique'
        db.delete_table(u'ref_objectif_strategique')

        # Deleting model 'Thematique'
        db.delete_table(u'ref_thematique')

        # Deleting model 'ProjetUp'
        db.delete_table('managedref_projetup')

        # Deleting model 'Poste'
        db.delete_table(u'ref_poste')

        # Deleting model 'ProjetPoste'
        db.delete_table(u'ref_projet_poste')

        # Deleting model 'Region'
        db.delete_table(u'ref_region')

        # Deleting model 'Bureau'
        db.delete_table(u'ref_bureau')

        # Deleting model 'Implantation'
        db.delete_table(u'ref_implantation')

        # Deleting model 'Pays'
        db.delete_table(u'ref_pays')

        # Deleting model 'Etablissement'
        db.delete_table(u'ref_etablissement')


    models = {
        'managedref.authentification': {
            'Meta': {'ordering': "['id']", 'object_name': 'Authentification', 'db_table': "u'ref_authentification'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'courriel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Employe']", 'primary_key': 'True', 'db_column': "'id'"}),
            'motdepasse': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'managedref.bureau': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Bureau', 'db_table': "u'ref_bureau'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Implantation']", 'db_column': "'implantation'"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom_court': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nom_long': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Region']", 'db_column': "'region'"})
        },
        'managedref.discipline': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Discipline', 'db_table': "u'ref_discipline'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom_court': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nom_long': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'managedref.employe': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Employe', 'db_table': "u'ref_employe'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'courriel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_entree': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fonction': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lieu_travail_theorique_de'", 'db_column': "'implantation'", 'to': "orm['managedref.Implantation']"}),
            'implantation_physique': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lieu_travail_reel_de'", 'db_column': "'implantation_physique'", 'to': "orm['managedref.Implantation']"}),
            'mandat_debut': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'mandat_fin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'poste_type_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poste_type_1'", 'blank': 'True', 'null': 'True', 'db_column': "'poste_type_1'", 'to': "orm['managedref.PosteType']"}),
            'poste_type_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poste_type_2'", 'blank': 'True', 'null': 'True', 'db_column': "'poste_type_2'", 'to': "orm['managedref.PosteType']"}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'responsable': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'responsable_de'", 'blank': 'True', 'null': 'True', 'db_column': "'responsable'", 'to': "orm['managedref.Employe']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Service']", 'db_column': "'service'"}),
            'telephone_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'telephone_poste': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'managedref.etablissement': {
            'Meta': {'ordering': "['pays__nom', 'nom']", 'object_name': 'Etablissement', 'db_table': "u'ref_etablissement'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cedex': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'blank': 'True', 'null': 'True', 'db_column': "'implantation'", 'to': "orm['managedref.Implantation']"}),
            'membre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'membre_adhesion_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to_field': "'code'", 'db_column': "'pays'", 'to': "orm['managedref.Pays']"}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'blank': 'True', 'null': 'True', 'db_column': "'region'", 'to': "orm['managedref.Region']"}),
            'responsable_genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'responsable_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_prenom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'managedref.groupeadmregion': {
            'Meta': {'object_name': 'GroupeAdmRegion', 'db_table': "u'ref_groupe_adm_region'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'employe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Employe']", 'db_column': "'employe'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Region']", 'db_column': "'region'"})
        },
        'managedref.groupearh': {
            'Meta': {'object_name': 'GroupeArh', 'db_table': "u'ref_groupe_arh'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'employe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Employe']", 'db_column': "'employe'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'managedref.groupecomptable': {
            'Meta': {'object_name': 'GroupeComptable', 'db_table': "u'ref_groupe_comptable'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'employe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Employe']", 'db_column': "'employe'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'managedref.groupecomptablelocal': {
            'Meta': {'object_name': 'GroupeComptableLocal', 'db_table': "u'ref_groupe_comptable_local'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'employe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Employe']", 'db_column': "'employe'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'managedref.groupecomptableregional': {
            'Meta': {'object_name': 'GroupeComptableRegional', 'db_table': "u'ref_groupe_comptable_regional'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'employe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Employe']", 'db_column': "'employe'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'managedref.groupedirdelegprogrammereg': {
            'Meta': {'object_name': 'GroupeDirDelegProgrammeReg', 'db_table': "u'ref_groupe_dir_deleg_programme_reg'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'employe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Employe']", 'db_column': "'employe'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Region']", 'db_column': "'region'"})
        },
        'managedref.groupedirprogramme': {
            'Meta': {'object_name': 'GroupeDirProgramme', 'db_table': "u'ref_groupe_dir_programme'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'employe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Employe']", 'db_column': "'employe'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Service']", 'db_column': "'service'"})
        },
        'managedref.groupedirregion': {
            'Meta': {'object_name': 'GroupeDirRegion', 'db_table': "u'ref_groupe_dir_region'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'employe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Employe']", 'db_column': "'employe'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Region']", 'db_column': "'region'"})
        },
        'managedref.grouperespimplantation': {
            'Meta': {'object_name': 'GroupeRespImplantation', 'db_table': "u'ref_groupe_resp_implantation'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'employe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Employe']", 'db_column': "'employe'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Implantation']", 'db_column': "'implantation'"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'managedref.implantation': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Implantation', 'db_table': "u'ref_implantation'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'adresse_physique_bureau': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_code_postal': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'adresse_physique_code_postal_avant_ville': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'adresse_physique_no': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'adresse_physique_pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'impl_adresse_physique'", 'to_field': "'code'", 'db_column': "'adresse_physique_pays'", 'to': "orm['managedref.Pays']"}),
            'adresse_physique_precision': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_precision_avant': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_rue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'adresse_physique_ville': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'adresse_postale_boite_postale': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_bureau': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_code_postal': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_code_postal_avant_ville': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'adresse_postale_no': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'impl_adresse_postale'", 'to_field': "'code'", 'db_column': "'adresse_postale_pays'", 'to': "orm['managedref.Pays']"}),
            'adresse_postale_precision': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_precision_avant': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_rue': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adresse_postale_ville': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bureau_rattachement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Implantation']", 'db_column': "'bureau_rattachement'"}),
            'code_meteo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'commentaire': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'courriel': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'courriel_interne': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'date_extension': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_fermeture': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_inauguration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_ouverture': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fax_interne': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fuseau_horaire': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hebergement_convention': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'hebergement_convention_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hebergement_etablissement': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modif_date': ('django.db.models.fields.DateField', [], {}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom_court': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nom_long': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Region']", 'db_column': "'region'"}),
            'remarque': ('django.db.models.fields.TextField', [], {}),
            'responsable_implantation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'statut': ('django.db.models.fields.IntegerField', [], {}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'telephone_interne': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        'managedref.objectifspecifique': {
            'Meta': {'ordering': "['nom']", 'object_name': 'ObjectifSpecifique', 'db_table': "u'ref_objectif_specifique'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'objectif_strategique': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.ObjectifStrategique']", 'db_column': "'objectif_strategique'"})
        },
        'managedref.objectifstrategique': {
            'Meta': {'ordering': "['nom']", 'object_name': 'ObjectifStrategique', 'db_table': "u'ref_objectif_strategique'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'managedref.pays': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Pays', 'db_table': "u'ref_pays'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'unique': 'True'}),
            'code_bureau': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Bureau']", 'to_field': "'code'", 'null': 'True', 'db_column': "'code_bureau'", 'blank': 'True'}),
            'code_iso3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'unique': 'True'}),
            'developpement': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monnaie': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nord_sud': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Region']", 'db_column': "'region'"})
        },
        'managedref.poste': {
            'Meta': {'object_name': 'Poste', 'db_table': "u'ref_poste'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'managedref.postetype': {
            'Meta': {'object_name': 'PosteType', 'db_table': "u'ref_poste_type'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'managedref.programme': {
            'Meta': {'object_name': 'Programme', 'db_table': "u'ref_programme'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom_court': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nom_long': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'managedref.projet': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Projet', 'db_table': "u'ref_projet'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'date_debut': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_fin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'etablissement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Etablissement']", 'null': 'True', 'db_column': "'etablissement'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Implantation']", 'null': 'True', 'db_column': "'implantation'", 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'objectif_specifique': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.ObjectifSpecifique']", 'null': 'True', 'db_column': "'objectif_specifique'", 'blank': 'True'}),
            'partenaires': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'presentation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'managedref.projetcomposante': {
            'Meta': {'ordering': "['nom']", 'object_name': 'ProjetComposante', 'db_table': "u'ref_projet_composante'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom_court': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'projet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Projet']", 'db_column': "'projet'"})
        },
        'managedref.projetposte': {
            'Meta': {'object_name': 'ProjetPoste', 'db_table': "u'ref_projet_poste'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'code_bureau': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Bureau']", 'to_field': "'code'", 'db_column': "'code_bureau'"}),
            'code_poste': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Poste']", 'to_field': "'code'", 'db_column': "'code_poste'"}),
            'code_programme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Programme']", 'to_field': "'code'", 'db_column': "'code_programme'"}),
            'code_projet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Projet']", 'to_field': "'code'", 'db_column': "'code_projet'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'managedref.projetup': {
            'Meta': {'object_name': 'ProjetUp'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom_court': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'managedref.region': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Region', 'db_table': "u'ref_region'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation_bureau': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gere_region'", 'blank': 'True', 'null': 'True', 'db_column': "'implantation_bureau'", 'to': "orm['managedref.Implantation']"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'managedref.service': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Service', 'db_table': "u'ref_service'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'managedref.thematique': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Thematique', 'db_table': "u'ref_thematique'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'managedref.uniteprojet': {
            'Meta': {'ordering': "['nom']", 'object_name': 'UniteProjet', 'db_table': "u'ref_unite_projet'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'unique': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['managedref']
