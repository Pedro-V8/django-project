from asyncore import read
from pickletools import read_long1
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model
from models.posts.serializers import PostsSerializer
User = get_user_model()


class UsuarioSerializer(serializers.ModelSerializer):
    posts = PostsSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id','email', 'nome', 'age', 'posts' ,'nome_usuario','bio')


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'nome', 'password' ,'nome_usuario','bio','age')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data["age"] < 0:
            raise serializers.ValidationError("Campo 'age' não pode ser negativo")
        return data

    def create(self, validated_data):
        email = validated_data['email']
        nome = validated_data['nome']
        nome_usuario = validated_data['nome_usuario']
        password = validated_data['password']
        age = validated_data['age']
        bio = validated_data['bio']

        user = User.objects.create_user(email,
                                        nome,
                                        nome_usuario,
                                        password,
                                        bio,
                                        age)

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        print(user)
        if user and user.is_active:
            return user

        raise serializers.ValidationError('Incorrect credentials')

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()
