import logging
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.views.generic import FormView
from django.views.generic import ListView

from .models import Url
from .forms import UrlForm
from .filters import UrlFilter

logger = logging.getLogger(__name__)


class UrlView(ListView):
    model = Url
    template_name = 'index.html'

    @staticmethod
    def _get_url_page(url_list, page):
        paginator = Paginator(url_list, 5)
        try:
            url_list = paginator.page(page)
        except PageNotAnInteger:
            url_list = paginator.page(1)
        except EmptyPage:
            url_list = paginator.page(paginator.num_pages)
        return url_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        url_list = Url.objects.order_by('-publish_date').all()
        url_filter = UrlFilter(self.request.GET, queryset=url_list)
        context['url_list'] = self._get_url_page(url_filter.qs,
                                                 self.request.GET.get('page'))
        context['url_filter'] = url_filter
        context['form'] = url_filter.form
        return context


class AddUrlView(FormView):
    form_class = UrlForm
    template_name = 'urls_form.html'
    success_url = '/'

    def form_valid(self, form):
        context = self.get_context_data()
        context['form'] = form
        form.save()
        messages.success(self.request,
                         'Your new url: %s' % form.data.get('url'),
                         extra_tags='safe')
        return redirect('/', context)
