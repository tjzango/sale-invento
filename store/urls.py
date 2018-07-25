from django.conf.urls import url

from store.views import (
    store,
    item,
    add_item,
)


urlpatterns = [
    url(r'^$', store, name='index'),
    url(r'^add/item/$', add_item, name='add_item'),
    url(r'^item/(?P<value>[0-9]+)/$', item, name='item'),
]
