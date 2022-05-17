from django.db import models

class Account(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
