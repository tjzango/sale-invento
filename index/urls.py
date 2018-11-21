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
    index,
    report,
    profile,
    message,
    add_user,
    activate,
    deactivate,
    message_tag,
    report_week,
    add_employee,
    report_print,
    report_month,
    send_message,
    report_all_time,
    manage_employees,
    customer_requests,
    customer_request_order,
)

# this are the url patterns their name and view there are pointing with root url map
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^customer/request/$', customer_requests, name='customer_requests'),
    url(r'^request/order/customers/$', customer_request_order, name='customer_request_order'),

    url(r'^users/$', users, name='users'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^users/add/$', add_user, name='add_user'),
    url(r'^users/(?P<key>[0-9]+)/activate/$', activate, name='activate'),
    url(r'^users/(?P<key>[0-9]+)/deactivate/$', deactivate, name='deactivate'),

    url(r'^message/$', message, name='message'),
    url(r'^__tag/(?P<key>[0-9]+)/$', message_tag, name='message_tag'),
    url(r'^message/send/$', send_message, name='send_message'),

    url(r'report/$', report, name='report'),
    url(r'report/week/$', report_week, name='report_week'),
    url(r'report/month/$', report_month, name='report_month'),
    url(r'report/all/$', report_all_time, name='report_all_time'),
    url(r'^report/print/(?P<report_name>[A-Za-z0-9.-]+)/', report_print, name='report_'),

    url(r'^employee/$', manage_employees, name='employees'),
    url(r'^employee/add/$', add_employee, name='add_employee'),

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
