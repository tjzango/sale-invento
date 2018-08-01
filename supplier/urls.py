# The is the file responsible for url route in customer application
# it will join with muslim/urls application
from django.conf.urls import url

from supplier.views import (
    supplier,
    supplier_add,
    supplier_detail,

    order,
    order_stock,
    order_request,
)

# this are the url patterns their name and vue there pointing to
urlpatterns = [
    url(r'^$', supplier, name='index'),
    url(r'^add/', supplier_add, name='add'),
    url(r'^(?P<key>[0-9]+)/detail/', supplier_detail, name="detail"),

    url(r'^order/$', order, name='order'),
    url(r'^order/request', order_request, name="order_request"),
    url(r'^order/(?P<key>[0-9]+)/stock/', order_stock, name="order_stock")
]
