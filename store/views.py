from django.shortcuts import render

# Create your views here.

def index (request):
    """ A view to retuen the index page """
    return render(request, 'store/index.html')
