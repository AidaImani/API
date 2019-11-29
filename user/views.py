from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignupSerializer, LoginSerializer, ProfileChangeSerializer, ListOfUserSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class Signup(APIView):
    def post(self, request):
        signup_user = SignupSerializer(data=request.POST)
        if signup_user.is_valid():
            signup_user.save()
            res_signup = {'text': 'registered'}
            return Response(res_signup, status=200)


class Login(APIView):
    authentication_classes = []

    def post(self, request):
        user_login = LoginSerializer(data=request.POST)
        if user_login.is_valid():
            user = authenticate(
                                request,
                                username=request.POST['username'],
                                password=request.POST['password'])
            if user is None:
                return Response({'text': 'please first signup'}, status=401)
            if user:
                login(request, user)
                return Response({'data': {
                    'firstname': user.first_name,
                    'lastname': user.last_name,
                    'username': user.username,
                }})
        else:
            return Response(user_login.errors)


class Profile(APIView):
    def put(self, request):
        user_changable = ProfileChangeSerializer(instance=User.objects.get(id=request.data['id']), data=request.data)
        if user_changable.is_valid():
            user_changable.save()
            return Response({'text': 'your profile changed!'})
        else:
            return Response({'text': 'your data not valid!!!'})


class List_of_user(APIView):
    def get(self, request):
        users = User.objects.all()
        list_of_user = []
        for user in users:
            user = ListOfUserSerializer(user)
            u = user.data
            list_of_user.append(u)
        response = {'data': list_of_user}
        return Response(response)

