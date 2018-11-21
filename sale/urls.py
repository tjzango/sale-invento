# The is the file responsible for url route in customer application
# it will join with muslim/urls application
from django.conf.urls import url

from sale.views import (
    edit,
    index,
    remove,
    debtors,
    expense,
    invoice,
    new_sale,
    clear_cart,
    remove_item,
    debtors_info,
    add_item_to_cart,
    increase_quantity,
    decrease_quantity,
)

# this are the url patterns their name and vue there pointing to
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new/$', new_sale, name='new_sale'),
    url(r'^remove/(?P<key>[0-9]+)/$', remove, name='remove'),
    url(r'^invoice/(?P<key>[0-9]+)/$', invoice, name='invoice'),

    url(r'^expense/$', expense, name='expense'),

    url(r'^debtors/$', debtors, name='debtors'),
    url(r'^debtors/(?P<key>[0-9]+)/$', debtors_info, name='debtors'),

    url(r'^new/cart/clear/$', clear_cart, name='clear_cart'),
    url(r'^new/cart/(?P<key>[0-9]+)$', add_item_to_cart, name='cart'),
    url(r'^invoice/edit/(?P<key>[0-9]+)$', edit, name='edit'),
    url(r'^new/cart/clear/(?P<key>[0-9]+)/$', remove_item, name='remove_item'),
    url(r'^new/cart/(?P<key>[0-9]+)/(?P<quantity>[0-9]+)/-/$', decrease_quantity, name='cart_decrease'),
    url(r'^new/cart/(?P<key>[0-9]+)/(?P<quantity>[0-9]+)/+/$', increase_quantity, name='cart_increase'),
]
