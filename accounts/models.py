from django.db import models

class Account(models.Model):
    id = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
