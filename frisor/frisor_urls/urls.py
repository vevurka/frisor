from django.conf.urls import url

from . import views

app_name = 'frisor_urls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
