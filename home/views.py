from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('home/index.html', context_instance=RequestContext(request))

def artists(request):
    return render_to_response('home/artists.html', context_instance=RequestContext(request))

def history(request):
    return render_to_response('home/history.html', context_instance=RequestContext(request))
    
def contact(request):
    return render_to_response('home/contact.html', context_instance=RequestContext(request))
    
def tree(request):
    return render_to_response('home/tree.html', context_instance=RequestContext(request))