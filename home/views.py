from django.shortcuts import render_to_response
from django.template import RequestContext
from ozet.performances.models import Performance

def index(request):
  context = {}
  
  performances_q = Performance.objects.order_by('premier_date').reverse()
  if len(performances_q):
    context['last_performance'] = performances_q[0]
  
  return render_to_response('home/index.html', context, context_instance=RequestContext(request))
  
def artists(request):
  return render_to_response('home/artists.html', context_instance=RequestContext(request))
  
def history(request):
  return render_to_response('home/history.html', context_instance=RequestContext(request))