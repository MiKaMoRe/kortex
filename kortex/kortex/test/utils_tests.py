from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse
from kortex.test.views import HasPermissionsMixinView
from users.factories import UserFactory
from users.models import User


class TestHasPermissionsMixin(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserFactory()
        self.anonymouse_user = AnonymousUser()

    def test_has_permissions(self):
        self.assertEqual(HasPermissionsMixinView().has_permissions(self.user), True)
        self.assertEqual(
            HasPermissionsMixinView().has_permissions(self.anonymouse_user), False
        )

    def test_non_authenticated_user(self):
        """
        When non authenticated user tries to open page
        """
        resource = "has_permissions_mixin"
        request = self._get_resource(resource, AnonymousUser())
        response = HasPermissionsMixinView.as_view()(request)
        response.client = Client()
        redirect_url = "{url}?{query}".format(
            url=reverse("sign_in"), query=f"next=/{resource}"
        )
        self.assertRedirects(response, redirect_url)

    def test_conftest_authenticated_userirmed_user(self):
        """
        When authenticated user tries to open page
        """
        resource = "has_permissions_mixin"
        request = self._get_resource(resource, self.user)
        response = HasPermissionsMixinView.as_view()(request)
        response.client = Client()
        self.assertEqual(response.status_code, 200)

    def _get_resource(self, url, user: User):
        request = self.factory.get(url)
        request.user = user
        return request
