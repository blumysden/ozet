from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=200)
    permalink = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    lyrics = models.TextField(blank=True)
    score_dir = models.CharField(max_length=200, blank=True)
    in_songbook = models.BooleanField()
    transmission = models.BooleanField()

    def __unicode__(self):
        return self.title

class Recording(models.Model):
    music = models.ForeignKey('Music')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file_path = models.CharField(max_length=200)

    def __unicode__(self):
        music = Music.objects.get(pk=self.music_id)
        return "%s (from %s)" % (self.title, music.title)
  