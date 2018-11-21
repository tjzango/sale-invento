
# The is the file responsible for url route in customer application

# it will join with muslim/urls application
from django.conf.urls import url

# An import statement, It actually import the view that will be loaded if any url is requesteed
from customer.views import (
    customer,
    statement,
    customer_add
)

# this are the url patterns their name and vue there pointing to
urlpatterns = [
    url(r'^$', customer, name='index'),
    url(r'^add/$', customer_add, name='add'),
    url(r'^statement/(?P<key>[0-9]+)/$', statement, name='statement')
]
