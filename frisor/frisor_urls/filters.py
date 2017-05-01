from django_filters import FilterSet

from .models import Url


class UrlFilter(FilterSet):
    class Meta:
        model = Url
        fields = ['url', 'title', 'tags__name']
