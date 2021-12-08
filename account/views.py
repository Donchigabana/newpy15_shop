from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (RegisterSerializer, ActivationSerializer,
                          LoginSerializer, ChangePasswordSerializer,
                          ForgotPasswordSerializer)


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            message = f'Вы успешно зарегистрированы. ' \
                      f'Вам отправлено письмо с активацией'
            return Response(message, status=201)


class ActivationView(APIView):
    def post(self, request):
        data = request.data
        serializer = ActivationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Ваш аккаунт успешно активирован')


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    pass


class ChangePasswordView(APIView):
    pass


class ForgotPasswordView(APIView):
    pass

