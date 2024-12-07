from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from rest_framework.permissions import AllowAny


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.create_user(username=username, password=password)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response = Response({
            "detail": "User registered successfully"
        }, status=status.HTTP_201_CREATED)

        response.set_cookie('access_token', access_token, httponly=True, secure=False, samesite='None')
        response.set_cookie('refresh_token', str(refresh), httponly=True, secure=False, samesite='None')
        
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response['Access-Control-Allow-Credentials'] = 'true'

        return response


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response({"detail": "The user was not found"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response = Response({
            "detail": "User logged in successfully"
        }, status=status.HTTP_200_OK)

        response.set_cookie('access_token', access_token, httponly=True, secure=False, samesite='None')
        response.set_cookie('refresh_token', str(refresh), httponly=True, secure=False, samesite='None')
        
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response['Access-Control-Allow-Credentials'] = 'true'

        return response


class LogoutView(APIView):
    def post(self, request):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response['Access-Control-Allow-Credentials'] = 'true'
        
        return response
