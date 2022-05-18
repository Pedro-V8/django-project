from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=355)
    price = models.FloatField()

    def __str__(self):
        return self.title
