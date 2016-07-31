# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bureau',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('code', models.CharField(unique=True, max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('nom_court', models.CharField(max_length=255, blank=True)),
                ('nom_long', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'ordering': ['nom'],
                'verbose_name': 'bureau',
                'db_table': 'ref_bureau',
                'managed': True,
                'verbose_name_plural': 'bureaux',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('code', models.CharField(unique=True, max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('nom_long', models.CharField(max_length=255, blank=True)),
                ('nom_court', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'ordering': ['nom'],
                'db_table': 'ref_discipline',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('courriel', models.CharField(max_length=255, null=True, blank=True)),
                ('genre', models.CharField(max_length=3, choices=[('h', 'Homme'), ('f', 'Femme')])),
                ('fonction', models.CharField(max_length=255, null=True, blank=True)),
                ('telephone_poste', models.CharField(max_length=255, blank=True)),
                ('telephone_ip', models.CharField(max_length=255, blank=True)),
                ('telephone_ip_nomade', models.CharField(max_length=255, blank=True)),
                ('mandat_debut', models.DateField(null=True, blank=True)),
                ('mandat_fin', models.DateField(null=True, blank=True)),
                ('date_entree', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': ['nom'],
                'db_table': 'ref_employe',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('nom', models.CharField(max_length=255)),
                ('sigle', models.CharField(max_length=16, blank=True)),
                ('description', models.TextField(blank=True)),
                ('historique', models.TextField(blank=True)),
                ('nombre_etudiants', models.PositiveIntegerField(null=True, verbose_name="nombre d'\xe9tudiants", blank=True)),
                ('nombre_chercheurs', models.PositiveIntegerField(null=True, verbose_name='nombre de chercheurs', blank=True)),
                ('nombre_enseignants', models.PositiveIntegerField(null=True, verbose_name="nombre d'enseignants", blank=True)),
                ('nombre_membres', models.PositiveIntegerField(null=True, verbose_name='nombre de membres', blank=True)),
                ('membre', models.BooleanField()),
                ('membre_adhesion_date', models.DateField(null=True, verbose_name="date d'adh\xe9sion", blank=True)),
                ('statut', models.CharField(blank=True, max_length=1, null=True, choices=[(b'T', b'Titulaire'), (b'A', b'Associ\xc3\xa9'), (b'C', b'Candidat')])),
                ('qualite', models.CharField(blank=True, max_length=3, null=True, verbose_name='qualit\xe9', choices=[(b'ESR', b"\xc3\x89tablissement d'enseignement sup\xc3\xa9rieur et de recherche"), (b'CIR', b'Centre ou institution de recherche'), (b'RES', b'R\xc3\xa9seau')])),
                ('responsable_genre', models.CharField(max_length=1, verbose_name='genre', blank=True)),
                ('responsable_nom', models.CharField(max_length=255, verbose_name='nom', blank=True)),
                ('responsable_prenom', models.CharField(max_length=255, verbose_name='pr\xe9nom', blank=True)),
                ('responsable_fonction', models.CharField(max_length=255, verbose_name='fonction', blank=True)),
                ('responsable_courriel', models.EmailField(max_length=254, verbose_name='courriel', blank=True)),
                ('adresse', models.CharField(max_length=255, blank=True)),
                ('code_postal', models.CharField(max_length=20, verbose_name='code postal', blank=True)),
                ('cedex', models.CharField(max_length=20, verbose_name='CEDEX', blank=True)),
                ('ville', models.CharField(max_length=255, blank=True)),
                ('province', models.CharField(max_length=255, blank=True)),
                ('telephone', models.CharField(max_length=255, verbose_name='t\xe9l\xe9phone', blank=True)),
                ('fax', models.CharField(max_length=255, blank=True)),
                ('url', models.URLField(max_length=255, verbose_name='URL', blank=True)),
                ('date_modification', models.DateField(null=True, verbose_name='date de modification', blank=True)),
                ('commentaire', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['pays__nom', 'nom'],
                'abstract': False,
                'db_table': 'ref_etablissement',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GroupeAdmRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'db_table': 'ref_groupe_adm_region',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GroupeArh',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'db_table': 'ref_groupe_arh',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GroupeComptable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'db_table': 'ref_groupe_comptable',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GroupeComptableLocal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'db_table': 'ref_groupe_comptable_local',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GroupeComptableRegional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'db_table': 'ref_groupe_comptable_regional',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GroupeDirDelegProgrammeReg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'db_table': 'ref_groupe_dir_deleg_programme_reg',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GroupeDirProgramme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'db_table': 'ref_groupe_dir_programme',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GroupeDirRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'db_table': 'ref_groupe_dir_region',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GroupeRespImplantation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'db_table': 'ref_groupe_resp_implantation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Implantation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('nom', models.CharField(max_length=255)),
                ('nom_court', models.CharField(max_length=255, blank=True)),
                ('nom_long', models.CharField(max_length=255, blank=True)),
                ('type', models.CharField(max_length=255)),
                ('fuseau_horaire', models.CharField(max_length=255, blank=True)),
                ('code_meteo', models.CharField(max_length=255, blank=True)),
                ('responsable_implantation', models.IntegerField(null=True, blank=True)),
                ('adresse_postale_precision_avant', models.CharField(max_length=255, null=True, blank=True)),
                ('adresse_postale_no', models.CharField(max_length=30, null=True, blank=True)),
                ('adresse_postale_rue', models.CharField(max_length=255, null=True, blank=True)),
                ('adresse_postale_bureau', models.CharField(max_length=255, null=True, blank=True)),
                ('adresse_postale_precision', models.CharField(max_length=255, null=True, blank=True)),
                ('adresse_postale_boite_postale', models.CharField(max_length=255, null=True, blank=True)),
                ('adresse_postale_ville', models.CharField(max_length=255)),
                ('adresse_postale_code_postal', models.CharField(max_length=20, null=True, blank=True)),
                ('adresse_postale_code_postal_avant_ville', models.NullBooleanField()),
                ('adresse_postale_region', models.CharField(max_length=255, null=True, blank=True)),
                ('adresse_physique_precision_avant', models.CharField(max_length=255, blank=True)),
                ('adresse_physique_no', models.CharField(max_length=30, blank=True)),
                ('adresse_physique_rue', models.CharField(max_length=255, blank=True)),
                ('adresse_physique_bureau', models.CharField(max_length=255, blank=True)),
                ('adresse_physique_precision', models.CharField(max_length=255, blank=True)),
                ('adresse_physique_ville', models.CharField(max_length=255)),
                ('adresse_physique_code_postal', models.CharField(max_length=30, blank=True)),
                ('adresse_physique_code_postal_avant_ville', models.NullBooleanField()),
                ('adresse_physique_region', models.CharField(max_length=255, blank=True)),
                ('telephone', models.CharField(max_length=255, blank=True)),
                ('telephone_interne', models.CharField(max_length=255, blank=True)),
                ('fax', models.CharField(max_length=255, blank=True)),
                ('fax_interne', models.CharField(max_length=255, blank=True)),
                ('courriel', models.EmailField(max_length=254, blank=True)),
                ('courriel_interne', models.EmailField(max_length=254, blank=True)),
                ('url', models.URLField(max_length=255, blank=True)),
                ('statut', models.IntegerField(choices=[(0, 'Ferm\xe9e ou jamais ouverte'), (1, 'Ouverte'), (2, 'Ouverture imminente'), (3, 'En projet')])),
                ('date_ouverture', models.DateField(null=True, blank=True)),
                ('date_inauguration', models.DateField(null=True, blank=True)),
                ('date_extension', models.DateField(null=True, blank=True)),
                ('date_fermeture', models.DateField(null=True, blank=True)),
                ('hebergement_etablissement', models.CharField(max_length=255, blank=True)),
                ('hebergement_convention', models.NullBooleanField()),
                ('hebergement_convention_date', models.DateField(null=True, blank=True)),
                ('remarque', models.TextField()),
                ('commentaire', models.CharField(max_length=255, blank=True)),
                ('modif_date', models.DateField()),
            ],
            options={
                'ordering': ['nom'],
                'db_table': 'ref_implantation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ObjectifSpecifique',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('nom', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['nom'],
                'db_table': 'ref_objectif_specifique',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ObjectifStrategique',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['nom'],
                'db_table': 'ref_objectif_strategique',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('code', models.CharField(unique=True, max_length=2)),
                ('code_iso3', models.CharField(unique=True, max_length=3)),
                ('nom', models.CharField(max_length=255)),
                ('nord_sud', models.CharField(max_length=255, null=True, blank=True)),
                ('developpement', models.CharField(max_length=255, null=True, blank=True)),
                ('monnaie', models.CharField(max_length=255, null=True, blank=True)),
                ('code_bureau', models.ForeignKey(db_column=b'code_bureau', to_field=b'code', blank=True, to='references.Bureau', null=True)),
            ],
            options={
                'ordering': ['nom'],
                'verbose_name': 'pays',
                'db_table': 'ref_pays',
                'managed': True,
                'verbose_name_plural': 'pays',
            },
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('code', models.CharField(unique=True, max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'ref_poste',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PosteType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('nom', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'ref_poste_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('code', models.CharField(unique=True, max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('nom_long', models.CharField(max_length=255, blank=True)),
                ('nom_court', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'ref_programme',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('code', models.CharField(unique=True, max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('presentation', models.TextField(null=True, blank=True)),
                ('partenaires', models.TextField(null=True, blank=True)),
                ('service', models.CharField(blank=True, max_length=255, null=True, choices=[('1', 'Direction de la langue et de la communication scientifique en fran\xe7ais'), ('2', 'Direction du d\xe9veloppement et de la valorisation'), ('3', "Direction de l'innovation p\xe9dagogique et de l'\xe9conomie de la connaissance"), ('4', 'Direction du renforcement des capacit\xe9s scientifiques')])),
                ('date_debut', models.DateField(null=True, blank=True)),
                ('date_fin', models.DateField(null=True, blank=True)),
                ('etablissement', models.ForeignKey(db_column=b'etablissement', blank=True, to='references.Etablissement', null=True)),
                ('implantation', models.ForeignKey(db_column=b'implantation', blank=True, to='references.Implantation', null=True)),
                ('objectif_specifique', models.ForeignKey(db_column=b'objectif_specifique', blank=True, to='references.ObjectifSpecifique', null=True)),
            ],
            options={
                'ordering': ['nom'],
                'db_table': 'ref_projet',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProjetComposante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('code', models.CharField(max_length=10)),
                ('nom', models.CharField(max_length=255)),
                ('nom_court', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('projet', models.ForeignKey(to='references.Projet', db_column=b'projet')),
            ],
            options={
                'ordering': ['nom'],
                'db_table': 'ref_projet_composante',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProjetPoste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('code', models.CharField(unique=True, max_length=255)),
                ('code_bureau', models.ForeignKey(to='references.Bureau', db_column=b'code_bureau', to_field=b'code')),
                ('code_poste', models.ForeignKey(to='references.Poste', db_column=b'code_poste', to_field=b'code')),
                ('code_programme', models.ForeignKey(to='references.Programme', db_column=b'code_programme', to_field=b'code')),
                ('code_projet', models.ForeignKey(to='references.Projet', db_column=b'code_projet', to_field=b'code')),
            ],
            options={
                'db_table': 'ref_projet_poste',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProjetUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('code', models.CharField(unique=True, max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('nom_court', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('code', models.CharField(unique=True, max_length=255)),
                ('nom', models.CharField(max_length=255, db_index=True)),
                ('implantation_bureau', models.ForeignKey(related_name='gere_region', db_column=b'implantation_bureau', blank=True, to='references.Implantation', null=True)),
            ],
            options={
                'ordering': ['nom'],
                'verbose_name': 'r\xe9gion',
                'db_table': 'ref_region',
                'managed': True,
                'verbose_name_plural': 'r\xe9gions',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('nom', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['nom'],
                'db_table': 'ref_service',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Thematique',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('nom', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['nom'],
                'db_table': 'ref_thematique',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UniteProjet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True, editable=False)),
                ('code', models.CharField(unique=True, max_length=10)),
                ('nom', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['nom'],
                'db_table': 'ref_unite_projet',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ZoneAdministrative',
            fields=[
                ('actif', models.BooleanField(default=True, editable=False)),
                ('code', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('nom', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['nom'],
                'verbose_name': 'zone administrative',
                'db_table': 'ref_zoneadministrative',
                'managed': True,
                'verbose_name_plural': 'zones administratives',
            },
        ),
        migrations.CreateModel(
            name='Authentification',
            fields=[
                ('actif', models.BooleanField(default=True, editable=False)),
                ('id', models.ForeignKey(primary_key=True, db_column=b'id', serialize=False, to='references.Employe')),
                ('courriel', models.CharField(unique=True, max_length=255)),
                ('motdepasse', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'ref_authentification',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='pays',
            name='region',
            field=models.ForeignKey(to='references.Region', db_column=b'region'),
        ),
        migrations.AddField(
            model_name='objectifspecifique',
            name='objectif_strategique',
            field=models.ForeignKey(to='references.ObjectifStrategique', db_column=b'objectif_strategique'),
        ),
        migrations.AddField(
            model_name='implantation',
            name='adresse_physique_pays',
            field=models.ForeignKey(related_name='impl_adresse_physique', db_column=b'adresse_physique_pays', to_field=b'code', to='references.Pays'),
        ),
        migrations.AddField(
            model_name='implantation',
            name='adresse_postale_pays',
            field=models.ForeignKey(related_name='impl_adresse_postale', db_column=b'adresse_postale_pays', to_field=b'code', to='references.Pays'),
        ),
        migrations.AddField(
            model_name='implantation',
            name='bureau_rattachement',
            field=models.ForeignKey(db_column=b'bureau_rattachement', blank=True, to='references.Implantation', null=True),
        ),
        migrations.AddField(
            model_name='implantation',
            name='region',
            field=models.ForeignKey(to='references.Region', db_column=b'region'),
        ),
        migrations.AddField(
            model_name='implantation',
            name='zone_administrative',
            field=models.ForeignKey(to='references.ZoneAdministrative'),
        ),
        migrations.AddField(
            model_name='grouperespimplantation',
            name='employe',
            field=models.ForeignKey(to='references.Employe', db_column=b'employe'),
        ),
        migrations.AddField(
            model_name='grouperespimplantation',
            name='implantation',
            field=models.ForeignKey(to='references.Implantation', db_column=b'implantation'),
        ),
        migrations.AddField(
            model_name='groupedirregion',
            name='employe',
            field=models.ForeignKey(to='references.Employe', db_column=b'employe'),
        ),
        migrations.AddField(
            model_name='groupedirregion',
            name='region',
            field=models.ForeignKey(to='references.Region', db_column=b'region'),
        ),
        migrations.AddField(
            model_name='groupedirprogramme',
            name='employe',
            field=models.ForeignKey(to='references.Employe', db_column=b'employe'),
        ),
        migrations.AddField(
            model_name='groupedirprogramme',
            name='service',
            field=models.ForeignKey(to='references.Service', db_column=b'service'),
        ),
        migrations.AddField(
            model_name='groupedirdelegprogrammereg',
            name='employe',
            field=models.ForeignKey(to='references.Employe', db_column=b'employe'),
        ),
        migrations.AddField(
            model_name='groupedirdelegprogrammereg',
            name='region',
            field=models.ForeignKey(to='references.Region', db_column=b'region'),
        ),
        migrations.AddField(
            model_name='groupecomptableregional',
            name='employe',
            field=models.ForeignKey(to='references.Employe', db_column=b'employe'),
        ),
        migrations.AddField(
            model_name='groupecomptablelocal',
            name='employe',
            field=models.ForeignKey(to='references.Employe', db_column=b'employe'),
        ),
        migrations.AddField(
            model_name='groupecomptable',
            name='employe',
            field=models.ForeignKey(to='references.Employe', db_column=b'employe'),
        ),
        migrations.AddField(
            model_name='groupearh',
            name='employe',
            field=models.ForeignKey(to='references.Employe', db_column=b'employe'),
        ),
        migrations.AddField(
            model_name='groupeadmregion',
            name='employe',
            field=models.ForeignKey(to='references.Employe', db_column=b'employe'),
        ),
        migrations.AddField(
            model_name='groupeadmregion',
            name='region',
            field=models.ForeignKey(to='references.Region', db_column=b'region'),
        ),
        migrations.AddField(
            model_name='etablissement',
            name='implantation',
            field=models.ForeignKey(related_name='+', db_column=b'implantation', blank=True, to='references.Implantation', null=True),
        ),
        migrations.AddField(
            model_name='etablissement',
            name='pays',
            field=models.ForeignKey(related_name='+', db_column=b'pays', to_field=b'code', to='references.Pays'),
        ),
        migrations.AddField(
            model_name='etablissement',
            name='region',
            field=models.ForeignKey(related_name='+', db_column=b'region', blank=True, to='references.Region', null=True, verbose_name=b'r\xc3\xa9gion'),
        ),
        migrations.AddField(
            model_name='employe',
            name='implantation',
            field=models.ForeignKey(related_name='lieu_travail_theorique_de', db_column=b'implantation', to='references.Implantation'),
        ),
        migrations.AddField(
            model_name='employe',
            name='implantation_physique',
            field=models.ForeignKey(related_name='lieu_travail_reel_de', db_column=b'implantation_physique', to='references.Implantation'),
        ),
        migrations.AddField(
            model_name='employe',
            name='poste_type_1',
            field=models.ForeignKey(related_name='poste_type_1', db_column=b'poste_type_1', blank=True, to='references.PosteType', null=True),
        ),
        migrations.AddField(
            model_name='employe',
            name='poste_type_2',
            field=models.ForeignKey(related_name='poste_type_2', db_column=b'poste_type_2', blank=True, to='references.PosteType', null=True),
        ),
        migrations.AddField(
            model_name='employe',
            name='responsable',
            field=models.ForeignKey(related_name='responsable_de', db_column=b'responsable', blank=True, to='references.Employe', null=True),
        ),
        migrations.AddField(
            model_name='employe',
            name='service',
            field=models.ForeignKey(to='references.Service', db_column=b'service'),
        ),
        migrations.AddField(
            model_name='bureau',
            name='implantation',
            field=models.ForeignKey(to='references.Implantation', db_column=b'implantation'),
        ),
        migrations.AddField(
            model_name='bureau',
            name='region',
            field=models.ForeignKey(to='references.Region', db_column=b'region'),
        ),
    ]
