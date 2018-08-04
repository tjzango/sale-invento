# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def index(request):
    """
    This view is responsible for loading the sale.html file
    :param request:
    :return:
    """
    return render(request, 'sale.html')