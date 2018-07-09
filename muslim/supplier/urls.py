from django.conf.urls import url

from supplier.views import (
    order,
    supplier,
    supplier_add,
    order_request,
    order_stock,
)


urlpatterns = [
    url(r'^$', supplier, name='index'),
    url(r'^add/', supplier_add, name='add'),
    url(r'^order/$', order, name='order'),
    url(r'^order/request', order_request, name="order_request"),
    url(r'^order/(?P<key>[0-9]+)/stock/', order_stock, name="order_stock")
]
