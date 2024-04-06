from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    


class Employee(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.FloatField(null=False)
    def __str__(self):
        return self.title