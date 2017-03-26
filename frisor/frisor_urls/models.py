from django.db import models


class Url(models.Model):
    url = models.URLField()
    publish_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    nick = models.CharField(max_length=200)

    @classmethod
    def create(cls, url="", title="", nick=""):
        url = cls(title=title, url=url, nick=nick)
        return url

