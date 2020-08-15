from django.db import models

class NotEmployed(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=200)
    image = models.CharField(max_length=50)

class Employed(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=200)
    image = models.CharField(max_length=50)