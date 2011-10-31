from django.conf.urls.defaults import *

urlpatterns = patterns('ozet.home.views',
    (r'^history', 'history'),
    (r'^artists', 'artists'),
    (r'^contact', 'contact'),
    (r'^$', 'index'),
)

