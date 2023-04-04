from user.models import User
from user.serializers import UserFlatSerializer
from django.contrib.auth.hashers import check_password

class UserService():
    def authenticate(username, password):
        user = User.objects.get(email=username)
        serializer = UserFlatSerializer(user).data
        print(password == serializer['password'])

        return check_password(password, serializer['password'])
