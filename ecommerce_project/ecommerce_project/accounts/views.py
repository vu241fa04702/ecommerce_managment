from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from .models import User
from .serializers import RegisterSerializer


class RegisterView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(APIView):

    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user:

            return Response(
                {
                    'message': 'Login Success',
                    'user_id': user.id,
                    'username': user.username,
                    'role': user.role
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                'message': 'Invalid Credentials'
            },
            status=status.HTTP_400_BAD_REQUEST
        )