import logging
from django.contrib import messages
from django.shortcuts import redirect
from django.views import View
from django.views.generic import FormView

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
