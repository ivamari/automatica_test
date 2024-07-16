from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from automatic.models import Worker


class PhoneAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None

        try:
            auth_type, phone_number = auth_header.split(' ', 1)
            if auth_type != 'Phone':
                raise AuthenticationFailed('Недопустимый тип аутентификации')
        except ValueError:
            raise AuthenticationFailed('Недопустимый формат заголовка авторизации')

        try:
            worker = Worker.objects.get(phone_number=phone_number)
        except Worker.DoesNotExist:
            raise AuthenticationFailed('Работник не найден')

        return (worker, None)


