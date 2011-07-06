from django.db import models

class LogEntry(models.Model):
    title = models.CharField(max_length=200)
    post_date = models.DateTimeField('post date')
    entry = models.TextField(blank=True)
    permalink = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.title
