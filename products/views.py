from django.shortcuts import render,get_object_or_404
from .models import product

# Create your views here.
def all_products(request):
    products =product.objects.all()
    context = {
        'products': products,
        
    }

    return render (request,'products/products.html',context)

def product_detail(request, product_id):
    productss = get_object_or_404(product, pk=product_id)

    context = {
        'product': productss,
    }

    return render(request, 'products/product_detail.html', context)
