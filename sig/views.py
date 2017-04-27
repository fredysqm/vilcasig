from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class sig_data_main(LoginRequiredMixin, TemplateView):
    template_name = 'sig/data/main.html'


class sig_client_main(LoginRequiredMixin, TemplateView):
    template_name = 'sig/client/main.html'