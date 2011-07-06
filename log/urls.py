from django.conf.urls.defaults import *

urlpatterns = patterns('ozet.log.views',
    (r'^entry/(?P<entry_id>[\w-]+)', 'entry'),
    (r'^(?P<page>[\w-]+)', 'log'),
)

