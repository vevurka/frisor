import logging
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.views import View
from django.views.generic import FormView
from django.views.generic import TemplateView

from .models import Url
from .forms import UrlForm

logger = logging.getLogger(__name__)


class UrlView(FormView):
    form_class = UrlForm
    template_name = 'index.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        url_list = Url.objects.order_by('-publish_date').all()
        paginator = Paginator(url_list, 2)
        page = self.request.GET.get('page')
        try:
            url_list = paginator.page(page)
        except PageNotAnInteger:
            url_list = paginator.page(1)
        except EmptyPage:
            url_list = paginator.page(paginator.num_pages)
        context['url_list'] = url_list
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        context['form'] = form
        form.save()
        messages.success(self.request,
                         'Your new url: %s' % form.data.get('url'),
                         extra_tags='safe')
        return redirect('/', context)