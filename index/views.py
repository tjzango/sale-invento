# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from index.models import Account, User

from index.forms import UserProfileForm


# Create your views here.
@login_required
def profile(request):
    """
    This view is responsible for
    :param request:
    :return:
    """
    form = UserProfileForm(request.POST or None, request.FILES)
    if form.is_valid():
        account = get_object_or_404(Account, user=request.user)
        account.user.first_name = form.cleaned_data.get("first_name")
        account.user.last_name = form.cleaned_data.get('last_name')
        account.contact = form.cleaned_data.get('contact')
        try:
            account.save()
            account.user.save()
            messages.success(request, "Updated basic information")
        except Exception as error:
            e = {'message': error}

            return redirect('/account')
    context = {'form': form}
    return render(request, 'profile.html', context)


def users(request):
    context = {
        'users': Account.objects.all()
    }
    return render(request, 'users.html', context)


def deactivate(request, key):
    user = User.objects.get(id=key)
    if user.is_staff:
        messages.error(request, 'Cannot deactivate superuser')
        return users(request)
    user.is_active = False
    user.save()
    return users(request)


def activate(request, key):
    user = User.objects.get(id=key)
    user.is_active = True
    user.save()
    return users(request)
