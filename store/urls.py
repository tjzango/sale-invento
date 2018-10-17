# The is the file responsible for url route in customer application
# it will join with muslim/urls application
from django.conf.urls import url

from store.views import (
    store,
    item,
    add_item,
)

# this are the url patterns their name and vue there pointing to
urlpatterns = [
    url(r'^$', store, name='index'),
    url(r'^add/item/$', add_item, name='add_item'),
    url(r'^item/(?P<value>[0-9]+)/$', item, name='item'),
]
