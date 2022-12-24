from django.views import View
from django.http import HttpResponse
from kortex.utils import HasPemissionsMixin
from users.models import User

"""
This is test views. It's available only in tests
"""


class HasPermissionsMixinView(HasPemissionsMixin, View):
    urls = "kortex.test.urls"
    login_url = "sign_in"

    def get(self, request):
        return HttpResponse()

    def has_permissions(self, user: User) -> bool:
        if user.is_authenticated:
            return True
        return False
