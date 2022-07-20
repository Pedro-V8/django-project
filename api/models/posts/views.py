
from rest_framework.response import Response
from .serializers import PostsSerializer , RegisterOrUpdatePostsSerializer
from rest_framework.views import APIView
from models.posts.models import Post
from models.user.views import User
from models.user.serializers import UsuarioSerializer

# Create your views here.

class PostsView(APIView):
    def post(self , request):
        
        serializer = RegisterOrUpdatePostsSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):

            user = User.objects.get(email=request.data["user_email"])
                
            
            post = Post.objects.create(
                title=request.data["title"], 
                content=request.data["content"],
                user=user)
            postJson = PostsSerializer(post)
                
            return Response(postJson.data)
                

            
            

        return Response("ok")

class PostDetailView(APIView):
    def get(self,request,pk,format=None):
        post = Post.objects.get(id=pk)
        
        serializer = PostsSerializer(post,many=False)
        
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        post = Post.objects.get(id=pk)
        serializer = RegisterOrUpdatePostsSerializer(instance=post,data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

    def delete(self,request,pk,format=None):
        post = Post.objects.get(id=pk)
        post.delete()
        return Response("Deleted")