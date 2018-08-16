# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from index.models import Account, User, Employee, Message

from index.forms import UserProfileForm, EmployeeForm, UserAddForm, MessageForm


# Create your views here.
@login_required
def add_user(request):
    form = UserAddForm(request.POST or None)
    if form.is_valid():
        account = form.save(commit=False)
        password = form.cleaned_data.get('password')
        password_ = form.cleaned_data.get('password_')
        username = form.cleaned_data.get('username')
        if account.employee:
            employee = Account.objects.filter(employee=account.employee)
            if employee.count() >= 1:
                messages.error(request, "Employee already exist")
                return redirect('/users/add/')

        if username:
            user_name = User.objects.filter(username=username)
            if user_name:
                messages.error(request, "Username already exist")
                return redirect('/users/add/')
        if password != password_:
            messages.error(request, "Passwords does not match")
            return redirect('/users/add/')
        if len(password) <= 5:
            messages.error(request, "Passwords must contain at least 6 characters")
            return redirect('/users/add/')
        if (account.employee.level == 'Cleaner') | (account.employee.level == 'Other'):
            messages.error(request, "This emplyee can't use the system\nCleaner or other")
            return redirect('/users/add')
        user = User.objects.create(
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name'),
            username=username
        )
        user.set_password(form.cleaned_data.get('username'))
        account.user = user
        account.save()
        return redirect('/users/')
    context = {
        'form': form
    }
    return render(request, 'add_user.html', context)


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


@login_required
def users(request):
    usr = Account.objects.all()
    context = {
        'users': usr,
        'active': usr.filter(user__is_active=True),
        'inactive': usr.filter(user__is_active=False)
    }
    return render(request, 'users.html', context)


@login_required
def deactivate(request, key):
    user = User.objects.get(id=key)
    if user.is_staff:
        messages.error(request, 'Cannot deactivate superuser')
        return users(request)
    user.is_active = False
    user.save()
    return users(request)


@login_required
def activate(request, key):
    user = User.objects.get(id=key)
    user.is_active = True
    user.save()
    return users(request)


@login_required
def manage_employees(request):
    employee = Employee.objects.all()
    acc = Account.objects.all().count()
    context = {
        'employees': employee,
        'non_users_emp': employee.count() - acc,
        'users_emp': acc
    }
    return render(request, 'employee.html', context)


@login_required
def add_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Add employee {}'.format(form.cleaned_data['name']))
        return redirect("/employee")
    context = {
        "form": form,
    }
    return render(request, 'add_employee.html', context)


@login_required
def message(request):
    context = {
        'message_set': Message.objects.all()
    }
    return render(request, 'messages_set.html', context)


@login_required
def send_message(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully send message')
        return redirect('/message')
    context = {
        'form': form
    }
    return render(request, 'message.html', context)


@login_required
def message_tag(request, key):
    _message = Message.objects.get(id=key)
    _message.visible = False
    _message.save()
    return redirect('/sale')

