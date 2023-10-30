from .serializers import UserSerializer,myTokenObtainPairSerializer
from .models import User
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = myTokenObtainPairSerializer

class UserRegister(CreateAPIView):
    serializer_class = UserSerializer

class UserList(ListCreateAPIView):
    queryset = User.objects.all().exclude(is_superuser=True)
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['email', 'username']

class UserDetails(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    print("-------- view ----------")
    def get_object(self):
        user_id = self.kwargs.get('id')
        user = get_object_or_404(User, id=user_id)
        print("---------", user)
        return user

    def perform_update(self, serializer):
        # Your custom update logic in the serializer
        serializer.save()


