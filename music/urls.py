from django.conf.urls.defaults import *

urlpatterns = patterns('ozet.music.views',
    (r'^songbook/(?P<permalink>[\w-]+)', 'songbook'),
    (r'^transmissions/(?P<permalink>[\w-]+)', 'transmissions'),
    (r'^transmissions', 'transmissions'),
    (r'^$', 'index'),
)