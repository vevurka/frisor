from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('frisor_urls.urls')),
    url(r'^admin/', admin.site.urls),
]