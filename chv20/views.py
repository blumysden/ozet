from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

SCENE_ORDER = [
    {
        "template": "chv20/arrival.html",
        "title": "The Arrival"
    },
    {
        "template": "chv20/lullaby.html",
        "title": "Lullaby from the First Generation to the Last"
    },
    {
        "template": "chv20/councilor.html",
        "title": "The Councilor's Speech"
    },
    {
        "template": "chv20/ode.html",
        "title": "An Ode to Our Travellers of the Constellations"
    },
    {
        "template": "chv20/mayor.html",
        "title": "The Mayor Speaks"
    },
    {
        "template": "chv20/villager_actions.html",
        "title": "Villager Actions"
    },
    {
        "template": "chv20/overheard.html",
        "title": "Overheard"
    }
]

def playbook(request):
    context = {
        "scenes": SCENE_ORDER
    }
    return render_to_response('chv20/playbook.html', context, \
        context_instance=RequestContext(request))

def community(request):
    return render_to_response('chv20/community.html', context_instance=RequestContext(request))