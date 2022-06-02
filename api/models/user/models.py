from re import S
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,
                    email,
                    nome,
                    password,
                    age):

        if not email or not password:
            raise ValueError('Usuários devem ter email e senha')

        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
            age=age
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)

    nome = models.TextField()
    age = models.IntegerField()

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
