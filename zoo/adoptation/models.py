from django.db import models
from model_utils.managers import InheritanceManager
# Create your models here.

class Adopter(models.Model):
    name = models.CharField(max_length=200)
    ssn = models.CharField(max_length=10, unique=True)

    def __repr__(self):
        return "Adopter: %s" % self.name

    def __str__(self):
        return "Adopter: %s" % self.name


class Animal(models.Model):
    objects = InheritanceManager()
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(default=1)
    adopter = models.ForeignKey(Adopter,on_delete=models.DO_NOTHING, null= True)

class Dog(Animal):

    def __repr__(self):
        return "Dog: %s" % self.name

    def __str__(self):
        return "Dog: %s" % self.name



class Cat(Animal):
    #representation in other things(list, tuple and ...)
    def __repr__(self):
        return "Cat: %s" % self.name
        # return f"Cat: {self.name}"
    #single
    def __str__(self):
        return "Cat: %s" % self.name



