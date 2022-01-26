from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST


from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings


from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import product
from bag.contexts import bag_contents

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
         messages.error(request, "There's nothing in your bag at the moment")
         return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KLyKFJs0stgofJHHPjoPZQdthBt6CnGr34zFmmu1lxXC5ppTv9FF1zgKUfXWicA4uY9KmQiM3fyvGsybuiQaS3W00n3B3PFYH',
        'client_secret': 'test client secret',
    }


        
    return render(request, template, context)



