from django.shortcuts import render

# Create your views here.
def views_bag(request):
    return render (request,'bag/bag.html')
