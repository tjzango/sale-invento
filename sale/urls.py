# The is the file responsible for url route in customer application
# it will join with muslim/urls application
from django.conf.urls import url

from sale.views import (
    index,
    new_sale,
    remove_item,
    increase_quantity,
    decrease_quantity,
    add_item_to_cart,
    clear_cart,
)

# this are the url patterns their name and vue there pointing to
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new/$', new_sale, name='new_sale'),
    url(r'^new/cart/(?P<key>[0-9]+)/(?P<quantity>[0-9]+)/-/$', decrease_quantity, name='cart_decrease'),
    url(r'^new/cart/(?P<key>[0-9]+)/(?P<quantity>[0-9]+)/+/$', increase_quantity, name='cart_increase'),
    url(r'^new/cart/(?P<key>[0-9]+)$', add_item_to_cart, name='cart'),
    url(r'^new/cart/clear/$', clear_cart, name='clear_cart'),
    url(r'^new/cart/clear/(?P<key>[0-9]+)/$', remove_item, name='remove_item'),
]
