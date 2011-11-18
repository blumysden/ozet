from django.conf.urls.defaults import *

urlpatterns = patterns('ozet.chv20.views',
    (r'^playbook', 'playbook'),
    (r'^community', 'community'),
)