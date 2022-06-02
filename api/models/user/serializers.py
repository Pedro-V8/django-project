from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'nome', 'age')


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'nome', 'age', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data["age"] < 0:
            raise serializers.ValidationError("Campo 'age' não pode ser negativo")
        return data

    def create(self, validated_data):
        email = validated_data['email']
        nome = validated_data['nome']
        password = validated_data['password']
        age = validated_data['age']

        user = User.objects.create_user(email,
                                        nome,
                                        password,
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
