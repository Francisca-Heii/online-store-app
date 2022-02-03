from django.db import models

# Create your models here.

class Person(models.Model):
    firstname = models.CharField(max_length=130,)
    lastname = models.CharField(max_length=130)
    occupation=models.CharField(max_length=130, default='', blank=True, )
    email = models.EmailField(blank=True, primary_key = True)
    feedback = models.TextField(blank=True)


class Enquiry(models.Model):
    cname = models.CharField(max_length=130)
    etype=models.CharField(max_length=130, default='', blank=True,)
    email = models.EmailField(blank=True)
    econcern = models.TextField(blank=True)