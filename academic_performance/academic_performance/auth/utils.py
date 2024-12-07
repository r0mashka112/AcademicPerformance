from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken


class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('access_token')
        if token:
            try:
                access_token = AccessToken(token)
            except Exception as e:
                raise AuthenticationFailed(f'Invalid token: {str(e)}')

            return self.get_user(access_token), access_token

        return None
