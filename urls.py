from django.conf.urls.defaults import *
from django.shortcuts import render_to_response
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^talentos/', include('talentos.foo.urls')),
    (r'^talentos/$', 'talentos.informacoes.views.exibir_formulario_conhecimento'),
    (r'^talentos/executar/$', 'talentos.informacoes.views.executar_formulario_conhecimento'),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'login/', 'django.contrib.auth.views.login')
)
