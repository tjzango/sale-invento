# The is the file responsible for url route in customer application
# it will join with muslim/urls application
from django.conf.urls import url
# An import statement, It actually import the view that will be loaded if any url is requested
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

from index.views import (
    users,
    profile,
    activate,
    deactivate,
    manage_employees,
)

# this are the url patterns their name and view there are pointing with root url map
urlpatterns = [
    url(r'^users/$', users, name='users'),
    url(r'^users/(?P<key>[0-9]+)/deactivate/$', deactivate, name='deactivate'),
    url(r'^users/(?P<key>[0-9]+)/activate/$', activate, name='activate'),
    url(r'^profile/$', profile, name='profile'),

    # Employee
    url(r'^employee/$', manage_employees, name='employees'),

    # logging<
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
