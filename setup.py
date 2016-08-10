# encoding: utf-8

from setuptools import setup, find_packages

name = 'auf.django.references'
version = '0.28'

setup(
    name=name,
    version=version,
    description="Modèles Django pour les données de référence de l'AUF",
    author='Éric Mc Sween',
    author_email='eric.mcsween@auf.org',
    url='http://pypi.auf.org/%s' % name,
    license='GPL',
    packages=find_packages(exclude=['tests', 'tests.*']),
    namespace_packages=['auf', 'auf.django'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ]
)
