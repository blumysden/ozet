from django.db import models

# Create your models here.

class Performance(models.Model):
    title = models.CharField(max_length=200)
    premier_date = models.DateTimeField('first performance date')
    last_date = models.DateTimeField('most recent performance date')
    description = models.TextField(blank=True)
    cast = models.TextField(blank=True)
    crew = models.TextField(blank=True)
    venue = models.ForeignKey('Venue')
    permalink = models.CharField(max_length=200, unique=True)
    flickr_photoset_id = models.IntegerField(blank=True)

    def __unicode__(self):
        return self.title
    
class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
    
class Video(models.Model):
    CATEGORY_CHOICES = (
            ('film', 'Film'),
            ('live', 'Live'),
        )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    performance = models.ForeignKey('Performance', blank=True, null=True)
    category = models.CharField(max_length=70, choices=CATEGORY_CHOICES)
    # url = models.URLField()
    url = models.CharField(max_length=200)

    def __unicode__(self):
        if self.performance_id:
            performance = Performance.objects.get(pk=self.performance_id)
            performance_title = " (from %s)" % performance.title
        else:
            performance_title = ""
        return "%s%s" % (self.title, performance_title)

class NPVideo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField()

    def __unicode__(self):
        return self.title

        
class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    performance = models.ForeignKey('Performance')
    file_path = models.CharField(max_length=200)
    thumb_path = models.CharField(max_length=200)

    def __unicode__(self):
        performance = Performance.objects.get(pk=self.performance_id)
        return "%s (from %s)" % (self.title, performance.title)