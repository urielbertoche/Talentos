from django.conf.urls.defaults import *
from django.shortcuts import render_to_response
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^talentos/$', 'talentos.informacoes.views.exibir_formulario_conhecimento'),
    (r'^talentos/executar/$', 'talentos.informacoes.views.executar_formulario_conhecimento'),

    (r'^admin/', include(admin.site.urls)),

    (r'login/', 'django.contrib.auth.views.login')
)


# MEDIA 
if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
