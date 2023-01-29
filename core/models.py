from django.db import models

# Create your models here.

class Information(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='img')


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    phone = models.IntegerField(default=0)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    quary = models.TextField()

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    decs = models.TextField()
    img = models.ImageField(upload_to='teacher')

class CourseList(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='course')