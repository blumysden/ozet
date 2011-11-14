from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

SCENE_ORDER = [
    {
        "template": "chv20/councilor.html",
        "title": "The Councilor's Speech"
    }
]

def playbook(request):
    context = {
        "scenes": SCENE_ORDER
    }
    return render_to_response('chv20/playbook.html', context, \
        context_instance=RequestContext(request))
