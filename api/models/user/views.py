from .models import User
from .serializers import RegistroSerializer, UsuarioSerializer , LoginSerializer


from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class UserView(APIView):

    def get(self , request , format=None):
        users = User.objects.all()
        serializer = UsuarioSerializer(users , many=True)
        return Response(serializer.data)

    
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
    #serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data

        userJSON = UsuarioSerializer(user)

        return Response({
            'user': userJSON.data
        })

        
        
