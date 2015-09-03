from django.contrib.auth import SESSION_KEY
from django.utils.functional import SimpleLazyObject
from django_mongoengine.auth.backends import get_user

__author__ = 'Gorman'


class AuthenticationMiddleware(object):
    def process_request(self, request):
        assert hasattr(request, 'session'), (
            "The Django authentication middleware requires session middleware "
            "to be installed. Edit your MIDDLEWARE_CLASSES setting to insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'django.contrib.auth.middleware.AuthenticationMiddleware'."
        )
        request.user = SimpleLazyObject(lambda: get_user(_get_user_session_key(request)))

from bson.objectid import ObjectId
def _get_user_session_key(request):
    # This value in the session is always serialized to a string, so we need
    # to convert it back to Python whenever we access it.
    if SESSION_KEY in request.session:
        return ObjectId(request.session[SESSION_KEY])