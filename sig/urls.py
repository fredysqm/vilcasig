from django.conf.urls import url
from sig.views import *


urlpatterns = [
    url(r'^$', sig_data_main.as_view(), name='sig_data_main'),

    url(r'^sigclient/$', sig_client_main.as_view(), name='sig_client_main'),

    #url(r'^error404/$', error404.as_view()),
    #url(r'^error500/$', error500.as_view()),
]