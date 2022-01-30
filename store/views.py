from django.shortcuts import render
from django.db.models import Q
from products.models import product,Category
from django.db.models.functions import Lower
from django.conf import settings
import os

# Create your views here.
def index(request):
    
    return render(request,'store/index.html', locals())



