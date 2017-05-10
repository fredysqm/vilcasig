from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


#class sig_client_main(LoginRequiredMixin, TemplateView):
class sig_client_main(TemplateView):
    template_name = 'sig/client/main.html'