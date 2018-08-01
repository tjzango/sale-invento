# The is the file responsible for url route in customer application
# it will join with muslim/urls application
from django.conf.urls import url

from sale.views import (
    index,
)

# this are the url patterns their name and vue there pointing to
urlpatterns = [
    url(r'^$', index, name='index'),
]
