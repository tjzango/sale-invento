from django.conf.urls import url

from sale.views import (
    index,
)


urlpatterns = [
    url(r'^$', index, name='index'),
]
