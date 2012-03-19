# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Etablissement.responsable_fonction'
        db.add_column(u'ref_etablissement', 'responsable_fonction', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Etablissement.responsable_fonction'
        db.delete_column(u'ref_etablissement', 'responsable_fonction')


    models = {
        'managedref.authentification': {
            'Meta': {'ordering': "['id']", 'object_name': 'Authentification', 'db_table': "u'ref_authentification'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'courriel': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Employe']", 'primary_key': 'True', 'db_column': "'id'"}),
            'motdepasse': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'managedref.bureau': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Bureau', 'db_table': "u'ref_bureau'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
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
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
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
            'poste_type_1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'poste_type_1'", 'null': 'True', 'db_column': "'poste_type_1'", 'to': "orm['managedref.PosteType']"}),
            'poste_type_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'poste_type_2'", 'null': 'True', 'db_column': "'poste_type_2'", 'to': "orm['managedref.PosteType']"}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'responsable': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'responsable_de'", 'null': 'True', 'db_column': "'responsable'", 'to': "orm['managedref.Employe']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Service']", 'db_column': "'service'"}),
            'telephone_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'telephone_poste': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'managedref.etablissement': {
            'Meta': {'ordering': "['pays__nom', 'nom']", 'object_name': 'Etablissement', 'db_table': "u'ref_etablissement'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cedex': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'commentaire': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_modification': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'db_column': "'implantation'", 'to': "orm['managedref.Implantation']"}),
            'membre': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'membre_adhesion_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to_field': "'code'", 'db_column': "'pays'", 'to': "orm['managedref.Pays']"}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'qualite': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'db_column': "'region'", 'to': "orm['managedref.Region']"}),
            'responsable_fonction': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_genre': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'responsable_nom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsable_prenom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'statut': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
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
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'code_bureau': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Bureau']", 'to_field': "'code'", 'null': 'True', 'db_column': "'code_bureau'", 'blank': 'True'}),
            'code_iso3': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
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
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
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
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom_court': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nom_long': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'managedref.projet': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Projet', 'db_table': "u'ref_projet'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
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
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'code_bureau': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Bureau']", 'to_field': "'code'", 'db_column': "'code_bureau'"}),
            'code_poste': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Poste']", 'to_field': "'code'", 'db_column': "'code_poste'"}),
            'code_programme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Programme']", 'to_field': "'code'", 'db_column': "'code_programme'"}),
            'code_projet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['managedref.Projet']", 'to_field': "'code'", 'db_column': "'code_projet'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'managedref.projetup': {
            'Meta': {'object_name': 'ProjetUp'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nom_court': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'managedref.region': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Region', 'db_table': "u'ref_region'"},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implantation_bureau': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'gere_region'", 'null': 'True', 'db_column': "'implantation_bureau'", 'to': "orm['managedref.Implantation']"}),
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
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'references.bureau': {
            'Meta': {'managed': 'False', 'ordering': "['nom']", 'object_name': 'Bureau', 'db_table': "u'ref_bureau'", '_ormbases': ['managedref.Bureau'], 'proxy': 'True'}
        },
        'references.employe': {
            'Meta': {'managed': 'False', 'ordering': "['nom']", 'object_name': 'Employe', 'db_table': "u'ref_employe'", '_ormbases': ['managedref.Employe'], 'proxy': 'True'}
        },
        'references.etablissement': {
            'Meta': {'managed': 'False', 'ordering': "['pays__nom', 'nom']", 'object_name': 'Etablissement', 'db_table': "u'ref_etablissement'", '_ormbases': ['managedref.Etablissement'], 'proxy': 'True'}
        },
        'references.implantation': {
            'Meta': {'managed': 'False', 'ordering': "['nom']", 'object_name': 'Implantation', 'db_table': "u'ref_implantation'", '_ormbases': ['managedref.Implantation'], 'proxy': 'True'}
        },
        'references.objectifspecifique': {
            'Meta': {'managed': 'False', 'ordering': "['nom']", 'object_name': 'ObjectifSpecifique', 'db_table': "u'ref_objectif_specifique'", '_ormbases': ['managedref.ObjectifSpecifique'], 'proxy': 'True'}
        },
        'references.objectifstrategique': {
            'Meta': {'managed': 'False', 'ordering': "['nom']", 'object_name': 'ObjectifStrategique', 'db_table': "u'ref_objectif_strategique'", '_ormbases': ['managedref.ObjectifStrategique'], 'proxy': 'True'}
        },
        'references.pays': {
            'Meta': {'managed': 'False', 'ordering': "['nom']", 'object_name': 'Pays', 'db_table': "u'ref_pays'", '_ormbases': ['managedref.Pays'], 'proxy': 'True'}
        },
        'references.poste': {
            'Meta': {'managed': 'False', 'object_name': 'Poste', 'db_table': "u'ref_poste'", '_ormbases': ['managedref.Poste'], 'proxy': 'True'}
        },
        'references.postetype': {
            'Meta': {'managed': 'False', 'object_name': 'PosteType', 'db_table': "u'ref_poste_type'", '_ormbases': ['managedref.PosteType'], 'proxy': 'True'}
        },
        'references.programme': {
            'Meta': {'managed': 'False', 'object_name': 'Programme', 'db_table': "u'ref_programme'", '_ormbases': ['managedref.Programme'], 'proxy': 'True'}
        },
        'references.projet': {
            'Meta': {'managed': 'False', 'ordering': "['nom']", 'object_name': 'Projet', 'db_table': "u'ref_projet'", '_ormbases': ['managedref.Projet'], 'proxy': 'True'}
        },
        'references.region': {
            'Meta': {'managed': 'False', 'ordering': "['nom']", 'object_name': 'Region', 'db_table': "u'ref_region'", '_ormbases': ['managedref.Region'], 'proxy': 'True'}
        },
        'references.service': {
            'Meta': {'managed': 'False', 'ordering': "['nom']", 'object_name': 'Service', 'db_table': "u'ref_service'", '_ormbases': ['managedref.Service'], 'proxy': 'True'}
        }
    }

    complete_apps = ['managedref']
