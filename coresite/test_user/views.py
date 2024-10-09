from copyreg import pickle

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import User
from .serializer import UserSerializer
import pickle


class RegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request):
        # user_instance = User.objects.create(email=request.data['email'], username = request.data['username'])
        # print(user_instance.get_username)
        # del user_instance.get_username
        # print(user_instance.get_username)
        qs = User.objects.all()
        pickle.dumps(qs.query)


        # serializer = UserSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
