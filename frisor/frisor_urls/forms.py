
from django import forms
from .models import Url


class UrlForm(forms.ModelForm):
    url = forms.URLField(label='URL')
    title = forms.CharField(label='Title')
    nick = forms.CharField(label='Nick')

    class Meta:
        model = Url
        fields = ['url', 'title', 'nick']


