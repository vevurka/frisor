from django_filters import FilterSet, ModelChoiceFilter

from .models import Url, Tags


class UrlFilter(FilterSet):
    tags__name = ModelChoiceFilter(queryset=Tags.objects)

    class Meta:
        model = Url
        fields = {
            'url': ['contains'],
            'title': ['contains'],
        }
