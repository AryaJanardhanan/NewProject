from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    place = models.CharField(max_length=100)
    img = models.ImageField(upload_to='gallery/', default=0)
    fl = models.FileField(upload_to='documents/', default=0)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    name = models.CharField(max_length=150)
    pub_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
   