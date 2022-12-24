from django.urls import path
from kortex.test.views import HasPermissionsMixinView
from django.urls.resolvers import URLPattern

"""
This is test urls. It's available only in tests
"""

urlpatterns = [
    path(
        "has_permissions_mixin_path/",
        HasPermissionsMixinView.as_view(),
        name="has_permissions_mixin",
    )
]
