from django.shortcuts import get_object_or_404

from index.models import Account, Message


def user(request):



    if request.user.is_authenticated:
        try:
            user = get_object_or_404(Account, user=request.user)
        except Exception as e:
            return {'user': request.user}
        return {'user': user}
    return {'user': 'None'}


def message(request):
    if request.user.is_authenticated:
        try:
            usr = Account.objects.get(user=request.user)
            msg = Message.objects.filter(user=usr, visible=True)
        except Exception as e:
            return {'messages_not': {e}}
        return {'messages_not': msg}
    return {'messages_not': 'None'}
