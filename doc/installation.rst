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
