from django.conf.urls import url
from django.contrib.auth import views as auth_views
from sig.views import *


urlpatterns = [

    url(r'^accounts/login/$', auth_views.login, name='auth_login'),
    url(r'^accounts/logout/$', auth_views.logout, name='auth_logout'),

    url(r'^$', sig_data_main.as_view(), name='sig_data_main'),

    url(r'^sigclient/$', sig_client_main.as_view(), name='sig_client_main'),

    #url(r'^error404/$', error404.as_view()),
    #url(r'^error500/$', error500.as_view()),
]