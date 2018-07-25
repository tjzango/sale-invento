from index.models import Account
from django.shortcuts import get_object_or_404


def user(request):
    if request.user.is_authenticated:
        try:
            user = get_object_or_404(Account, user=request.user)
        except Exception as e:
            return {'user': request.user}
        return {'user': user}
    return {'user': 'None'}

