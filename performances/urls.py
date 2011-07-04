from django.conf.urls.defaults import *

urlpatterns = patterns('ozet.performances.views',
    (r'^(?P<permalink>[\w-]+)/photos', 'photos'),
    (r'^(?P<permalink>[\w-]+)', 'performance'),
    (r'^video', 'video'),
    (r'^$', 'index'),
)