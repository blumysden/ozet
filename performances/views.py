import re
from django.conf import settings
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from ozet.performances.models import Performance, Venue, Video, NPVideo

import flickrapi

def index(request):
    context = {}

    performances_q = Performance.objects.order_by('premier_date').reverse()
    context['performances'] = performances_q      
    return render_to_response('performances/performances.html', context, \
        context_instance=RequestContext(request))

def video(request):
    sort = request.GET.get('sort', 'category')
    if sort == 'category':
        return _video_by_category(request)
    elif sort == 'performance':
        return _video_by_performance(request)
        
def _video_by_performance(request):
    performances = []
    pids = []
    np_videos = Video.objects.filter(performance=None)
    videos_q = Video.objects.exclude(performance=None)
    for video in videos_q:
        pid = video.performance_id
        if pid not in pids:
            performances.append(Performance.objects.get(pk=pid)) 
            pids.append(pid)
    context = {
        'videos': videos_q,
        'performances': performances,
        'np_videos': np_videos
    }
    return render_to_response('performances/video.html', context, \
        context_instance=RequestContext(request))
        
def _video_by_category(request):
    categories = {}
    videos_q = Video.objects.all().order_by('performance')
    category_titles = {
        'film': 'Films',
        'live': 'Live Performances',
    }
    for video in videos_q:
        if video.category not in categories:
            categories[video.category] = {
                'title': category_titles[video.category],
                'videos': [video]
            }
        else:
            categories[video.category]['videos'].append(video)
    context = {
        'categories': categories,
    }
    return render_to_response('performances/video_by_category.html', context, \
        context_instance=RequestContext(request))

def performance(request, permalink):
    context = {}

    performance = get_object_or_404(Performance, permalink=permalink)

    context['performance'] = performance
    context['permalink'] = permalink
    htmlencode_fields = {
        'description': performance.description,
        'cast': performance.cast,
        'crew': performance.crew
    }
    for k, v in htmlencode_fields.items():
        if v:
            context[ '%s_html' % k ] = re.sub('\n', '<br/>', v)
            
    if performance.video_set.count():
        context['videos'] = [{
            'title': video.title,
            'url': video.url
        } for video in performance.video_set.all()]
    
    if performance.flickr_photoset_id:
        photos = _get_performance_photos(performance.flickr_photoset_id, 100)
        # context['photos'] = photos[0:5]
        # if len(photos) > 5:
        #     context['more_photos'] = True
        context['photos'] = photos

    return render_to_response('performances/performance.html', context, \
    context_instance=RequestContext(request))
    
def photos(request, permalink):
    context = {}

    performance = get_object_or_404(Performance, permalink=permalink)

    context['performance'] = performance
    return render_to_response('performances/photos.html', context, \
    context_instance=RequestContext(request))
    
def _get_performance_photos(photoset_id, limit=100):
    flickr = flickrapi.FlickrAPI(settings.FLICKRAPI_KEY)
    try:
        api_response = flickr.photosets_getPhotos(photoset_id=photoset_id, 
            per_page=limit, extras='url_t, url_m')
        photos = api_response.find('photoset').findall('photo')
        return [ photo.attrib for photo in photos ]
    except:
        return []