from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from datetime import datetime, date
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Publish(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='untitled')

    def __str__(self):
        return self.title + ' by ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
