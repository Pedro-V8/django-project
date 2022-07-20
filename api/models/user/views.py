from django.views import View
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import RegistroSerializer, UsuarioSerializer , LoginSerializer , TokenSerializer

# Create your views here.
class InitialPage(View):
    template = 'index.html'
    def get(self, request):
        teste = {
            'name': "Pedro",
            'age': 18
        }
        return render(request , self.template, teste)

class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self , request , format=None):
        
        users = User.objects.all()
        serializer = UsuarioSerializer(users , many=True)
        return Response(serializer.data)



class RegisterUserView(APIView):
    def post(self , request , format=None):
        print(request.data)
        serializer = RegistroSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        userJSON = UsuarioSerializer(user)

        return Response(userJSON.data)


class UserDetail(APIView):

    def get(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UsuarioSerializer(user, many=False)
        return Response(serializer.data)

    def post(self , request , format=None):
        print(request.data)
        serializer = RegistroSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        userJSON = UsuarioSerializer(user)

        return Response(userJSON.data)
    
    def put(self, request, pk, format=None):
        user = User.objects.get(id=pk)
        serializer = UsuarioSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        user = User.objects.get(id=pk)
        user.delete()

        return Response('Deleted')

class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        userT = User.objects.get(email=request.data["email"])
        userJSON = UsuarioSerializer(user)
        
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'user': userJSON.data,
            'token': token.key
        })

        
        
