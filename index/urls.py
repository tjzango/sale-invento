from django.conf.urls import url
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_change,
    password_reset_done,
    password_change_done,
    password_reset_confirm,
    password_reset_complete,
)

from index.views import profile


urlpatterns = [
    url(r'^profile/$', profile, name='profile'),
    # logging
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    # Change Password
    url(r'^password-change/$', password_change, name='password_change'),
    url(r'^password-change/done/$', password_change_done, name='password_change_done'),

    # forget Password
    url(r'^password-reset/$',
        password_reset,
        name='password_reset'),
    url(r'^password-reset/done/$',
        password_reset_done,
        name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
        password_reset_complete,
        name='password_reset_complete'),
]
