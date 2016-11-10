from django.conf.urls import url

from sig.views import *



urlpatterns = [
    url(r'^$', sig_main.as_view(), name='sig_main_url'),
    #url(r'^error404/$', error404.as_view()),
    #url(r'^error500/$', error500.as_view()),
]