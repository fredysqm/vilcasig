from django.views.generic import TemplateView


class sig_account_login(TemplateView):
    template_name = 'sig/account/login.html'

class sig_client_main(TemplateView):
    template_name = 'sigclient/main.html'