from django.views.generic import TemplateView


class sig_main(TemplateView):
    template_name = 'sig/main.html'

class sig_main2(TemplateView):
    template_name = 'sig/get_feature_info.html'

class sig_future(TemplateView):
    template_name = 'sig/future.html'