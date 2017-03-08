import logging

from django.shortcuts import render

from .models import Url

logger = logging.getLogger(__name__)


def index(request):
    url_list = Url.objects.order_by('-publish_date').all()
    context = {
        'url_list': url_list,
    }
    if request.method == 'POST':
        nick = request.POST['nick']
        url = request.POST['url']
        title = request.POST['title']
        logger.info("Creating an url for data: %s %s %s" % (nick, url, title))
        url = Url.create(url=url, title=title, creator=nick)
        url.save()

    return render(request, 'frisor_urls/index.html', context)
