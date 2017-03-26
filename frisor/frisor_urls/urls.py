from django.conf.urls import url
from .views import UrlView

from django.contrib import admin
admin.autodiscover()
app_name = 'frisor_urls'
urlpatterns = [
    url(r'^$', UrlView.as_view())
]
