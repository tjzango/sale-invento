from django.conf.urls import url

from customer.views import (
    customer,
    customer_add
)


urlpatterns = [
    url(r'^$', customer, name='index'),
    url(r'^add/', customer_add, name='add')
]
