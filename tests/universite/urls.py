from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView, UpdateView

from tests.universite.models import Universite
from tests.universite.forms import UniversiteForm

urlpatterns = patterns(
    '',
    url(r'^$', ListView.as_view(model=Universite), name='universite_list'),
    url(r'^(?P<pk>\d+)$',
        UpdateView.as_view(model=Universite, form_class=UniversiteForm),
        name='universite_update'),
)
