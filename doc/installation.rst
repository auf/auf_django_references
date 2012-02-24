Installation
============

Pour utiliser ce module, il suffit d'ajouter ``'auf.django.references'`` à la liste
``INSTALLED_APPS`` dans le fichier ``settings.py``::

    INSTALLED_APPS = (
        ...
        'auf.django.references',
        ...
    )

Certaines fonctionnalités nécessitent la publication de fichiers statiques
contenus dans le répertoire ``static`` de l'app ``auf.django.references``. La
meilleure façon de les rendre disponible est d'utiliser l'app
``django.contrib.staticfiles`` disponible à partir de Django 1.3. Si vous êtes
bloqués dans une version moins récente de Django, considérez l'utilisation de
l'app ``django-staticfiles`` qui offre les mêmes services.

Pour avoir réellement accès aux données de référence de l'AUF, il vous faut
avoir accès à la base de données MySQL nommée ``datamaster``. Cette base de
données est accessible sur les serveurs MySQL de développement et de production
de l'ARI. Les applications qui partagent ces serveurs ont donc accès aux données
de référence d'office. Pour déployer votre application sur un autre serveur ou
dans votre environnement de développement local, adressez-vous à l'ARI pour
obtenir une copie, synchronisée ou non, de ``datamaster``.

Une fois votre accès à ``datamaster`` assuré, il vous suffit de lancer la
commande ``bin/django syncdb`` pour créer des vues vers cette base de données
dans votre base de données, ce qui vous donne accès aux données de référence.
