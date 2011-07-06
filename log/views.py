from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ozet.log.models import LogEntry

def get_paginated_log_entries(page):
    context = {}
    log_entries_q = LogEntry.objects.order_by('post_date').reverse()
    paginator = Paginator(log_entries_q, 5)
    try:
        paginated_entries = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_entries = paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_entries = paginator.page(paginator.num_pages)
    return {
        'log_entries': paginated_entries.object_list,
        'log_pagination': paginated_entries
    }

def log(request, page):
    context = get_paginated_log_entries(page)
    return render_to_response('home/index.html', context, context_instance=RequestContext(request))

def entry(request, entry_id):
    context = {}
    return render_to_response('home/index.html', context, context_instance=RequestContext(request))
