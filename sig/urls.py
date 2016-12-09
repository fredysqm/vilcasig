from django.conf.urls import url
from sig.views import *


urlpatterns = [
    url(r'^$', sig_main.as_view(), name='sig_main_url'),
    url(r'^get_feature_info/$', sig_main2.as_view(), name='sig_main2_url'),
    url(r'^future/$', sig_future.as_view(), name='sig_future_url'),
    #url(r'^error404/$', error404.as_view()),
    #url(r'^error500/$', error500.as_view()),
]