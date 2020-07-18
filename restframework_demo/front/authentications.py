from rest_framework.authentication import BaseAuthentication
from django.core.cache import cache
from front.models import User

#http://127.0.0.1:8000/api/movies/?token='adfdsafsdafsaf'
class UserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.GET.get('token')
            user_id = cache.get(token)
            print(user_id)
            user = User.objects.get(pk=user_id)
            return user,token
        except Exception as e:
            return None

