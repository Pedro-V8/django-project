from re import S
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,
                    email,
                    nome,
                    nome_usuario,
                    password,
                    bio,
                    age):

        if not email or not password:
            raise ValueError('Usuários devem ter email e senha')

        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
            nome_usuario=nome_usuario,
            bio=bio,
            age=age
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)

    nome = models.TextField()
    nome_usuario = models.TextField()
    age = models.IntegerField()
    bio = models.TextField()

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nome
