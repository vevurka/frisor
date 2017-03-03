from django.db import models


class Url(models.Model):
    url = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')
    title = models.CharField(max_length=200)
    creator = models.CharField(max_length=200)
