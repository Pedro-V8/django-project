from rest_framework import serializers
from models.posts.models import Post

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title' , 'content', 'user']

class RegisterOrUpdatePostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title' , 'content']



