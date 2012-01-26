from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^references/', include('auf.django.references.urls')),
    (r'^', include(admin.site.urls)),
)
