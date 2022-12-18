from django.contrib.auth.mixins import AccessMixin
from django.http import JsonResponse
from users.models import User


class HasPemissionsMixin(AccessMixin):
    def has_permissions(self, user: User) -> bool:
        """
        Override this method to add custom permissions
        """
        return True

    def dispatch(self, request, *args, **kwargs):
        if self.has_permissions(request.user):
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context
