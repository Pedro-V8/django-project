from .models import User
from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from django.http import Http404

# Create your views here.
class UserView(APIView):

    def get(self , request , format=None):
        users = User.objects.all()
        serializer = UserSerializer(users , many=True)
        return Response(serializer.data)

    def post(self , request , format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        user = User.objects.get(id=pk)
        user.delete()

        return Response('Deleted')
