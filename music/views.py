import re
import os
from django.conf import settings
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from ozet.music.models import Music, Recording

def index(request):
    context = {
    'songbook_songs': [],
    'transmissions': []
    }

    music_q = Music.objects.order_by('title')

    for m in music_q:
        if m.in_songbook:
            context['songbook_songs'].append(m)
        if m.transmission:
            context['transmissions'].append(m)


    # context['songbook_songs'] = [ m for m in music_q if m.in_songbook ]

    return render_to_response('music/music.html', context, \
    context_instance=RequestContext(request))

def transmissions(request, permalink=None):
    context = {}
    music_q = Music.objects.order_by('id')
    context['transmissions'] = []
    for m in music_q:
        if m.transmission:
            item = {
                'title': m.title,
                'id': m.id
            }
            for recording in m.recording_set.all():
                item['path'] = recording.file_path
            context['transmissions'].append(item)
            if permalink == m.permalink:
                context['autoplay'] = m.id
    return render_to_response('music/transmissions.html', context, \
        context_instance=RequestContext(request))


def songbook(request, permalink):
    context = {}

    song = get_object_or_404(Music, permalink=permalink)

    context['song'] = song
    if song.lyrics:
        context['lyrics_html'] = re.sub('\n', '<br/>', song.lyrics)
    # count score pages
    if song.score_dir:
        score_files = os.listdir('%s/scores/%s/' % (settings.MEDIA_ROOT, song.score_dir))
        score_files.sort()
        context['score_files'] = score_files
    if song.recording_set.count():
        context['recordings'] = [{
            'title': recording.title,
            'path': recording.file_path
        } for recording in song.recording_set.all().order_by('id')] 

    return render_to_response('music/songbook.html', context, \
    context_instance=RequestContext(request))