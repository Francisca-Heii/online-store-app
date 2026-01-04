
# Create your models here.
from unicodedata import category
from unittest import skipUnless
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    class Meta():
        verbose_name_plural='Categories'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(max_length=254, unique=True, null=True, blank=True)  # Add this
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    

class product(models.Model):
    category=models.ForeignKey('Category',null=True,blank=True,on_delete=models.SET_NULL)
    sku=models.CharField(max_length=254,null=True,blank=True)
    name= models.CharField(max_length=254)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    rating=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    image_url=models.URLField(max_length=1024,null=True,blank=True)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name