from django.shortcuts import render_to_response
from django.template import RequestContext
from ozet.log.models import LogEntry
from ozet.log.views import get_paginated_log_entries

def index(request):
    context = get_paginated_log_entries(1)
    return render_to_response('home/index.html', context, context_instance=RequestContext(request))

def artists(request):
    return render_to_response('home/artists.html', context_instance=RequestContext(request))

def history(request):
    return render_to_response('home/history.html', context_instance=RequestContext(request))