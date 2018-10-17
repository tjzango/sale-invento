"""muslim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


"""
There are urls to other applications patterns example 
  url(r'^', include('index.urls')) is a link to index/urls.py
  which contain other urls route
"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('index.urls')),
    url(r'^sale/', include('sale.urls', namespace='sale')),
    url(r'^store/', include('store.urls', namespace='store')),
    url(r'^supplier/', include('supplier.urls', namespace='supplier')),
    url(r'^customer/', include('customer.urls', namespace='customer')),
]
