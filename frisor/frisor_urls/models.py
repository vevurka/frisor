from tagulous import models as tagulous_models
from django.db import models


class Tags(tagulous_models.TagModel):
    class TagMeta:
        initial = "programming"
        force_lowercase = True
        autocomplete_view = 'url_tags_autocomplete'


class Url(models.Model):
    url = models.URLField()
    publish_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    nick = models.CharField(max_length=200)
    tags = tagulous_models.TagField(Tags)

    @classmethod
    def create(cls, url="", title="", nick="", tags=None):
        url = cls(title=title, url=url, nick=nick, tags=None)
        return url
