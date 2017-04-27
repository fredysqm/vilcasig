from django.conf.urls import url
from django.contrib.auth import views as auth_views
from sig.views import *


urlpatterns = [

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^$', sig_account_login.as_view(), name='sig_data_main_url'),

    url(r'^sigclient/$', sig_client_main.as_view(), name='sig_client_main_url'),
    #url(r'^error404/$', error404.as_view()),
    #url(r'^error500/$', error500.as_view()),
]