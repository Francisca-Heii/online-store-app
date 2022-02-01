from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=130)
    last_name = models.CharField(max_length=130)
    occupation=models.CharField(max_length=130, default='', blank=True, )
    email = models.EmailField(blank=True)
    feedback = models.TextField(blank=True)


class Enquiry(models.Model):
    cname = models.CharField(max_length=130)
    etype=models.CharField(max_length=130, default='', blank=True, )
    email = models.EmailField(blank=True)
    econcern = models.TextField(blank=True)