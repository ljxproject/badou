from .models import User


class MobileBackend(object):
    def authenticate(**credentials):
        mobile = credentials.get('mobile', '')
        if mobile:
            try:
                user = User.objects.get(mobile=mobile)
            except User.DoesNotExist:
                pass
            else:
                if user.check_password(credentials['password']):
                    return user

    def get_user(self, user_id):

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
