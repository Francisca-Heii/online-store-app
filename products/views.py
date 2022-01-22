from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import product,Category

# Create your views here.
def all_products(request):
    products =product.objects.all()
    query = None
    categories=None
    
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,

        
    }

    return render (request,'products/products.html',context)

def product_detail(request, product_id):
    productss = get_object_or_404(product, pk=product_id)

    context = {
        'product': productss,
    }

    return render(request, 'products/product_detail.html', context)
