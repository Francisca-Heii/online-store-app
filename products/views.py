from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import product,Category
from django.db.models.functions import Lower


# # Create your views here.
# def all_products(request):
#     products = product.objects.all()
#     query = None
#     categories=None
#     sort=None
#     direction=None
    
#     if request.GET:
#         if 'sort' in request.GET:
#             sortkey = request.GET['sort']
#             sort = sortkey
#             if sortkey == 'name':
#                 sortkey = 'lower_name'
#                 products = products.annotate(lower_name=Lower('name'))
#             if sortkey == 'category':
#                 sortkey = 'category__name'
#             if 'direction' in request.GET:
#                 direction = request.GET['direction']
#                 if direction == 'desc':
#                     sortkey = f'-{sortkey}'
#             products = products.order_by(sortkey)

#         if 'category' in request.GET:
#             categories = request.GET['category'].split(',')
#             print("Total received",categories)
#             products = products.filter(category__name__in=categories)
#             categories =Category.objects.filter(name__in=categories)

        
#         if 'q' in request.GET:
#             category=['Sofa', 'TV Unit', 'Coffee Table', 'Beds', 'Matressess', 'Wardrobes', 'Dinning Tables', 'Dinning Chair', 'Dinning Set', 'Desk', 'Office Chair', 'Candles and Holders', 'Throws and Blankets', 'Table Lamp', 'Ornamental items', 'Ceiling Lamp', 'Floor Lamp']
#             category={"Sofa":"Sofa", "TV unit":"tv_unit", }
#             query = request.GET['q']
#             print("query ",query)
#             if not query:
#                 messages.error(request, "You didn't enter any search criteria!")
#                 return redirect(reverse('products'))
#             queries = Q(name__icontains=query) | Q(description__icontains=query)
#             products = products.filter(queries)
#             print("jajdksk",queries)
#     current_sorting = f'{sort}_{direction}'
            

#     context = {
#         'products': products,
#         'search_term': query,
#         'current_categories': categories,
#         'current_sorting': current_sorting,
#     }

#     return render (request,'products/products.html',context)









def all_products(request):
    products = product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            url_categories = request.GET['category'].split(',')
            print("DEBUG - URL categories:", url_categories)
            
            # Map URL slugs to actual category names
            slug_to_name = {
                'sofa': 'Sofa',
                'tv_unit': 'TV Unit',  # This was correct
                'coffee_table': 'Coffee Table',
                'beds': 'Beds',
                'mattresses': 'Mattresses',
                'matressess': 'Mattresses',
                'wardrobes': 'Wardrobes',
                'dining_tables': 'Dining Tables',
                'dinning_tables': 'Dining Tables',
                'dining_chair': 'Dining Chair',
                'dinning_chair': 'Dining Chair',
                'dining_set': 'Dining Set',
                'dinning_set': 'Dining Set',
                'desk': 'Desk',
                'office_chair': 'Office Chair',
                'candles_and_holders': 'Candles and Holders',
                'throws_and_blankets': 'Throws and Blankets',
                'table_lamp': 'Table Lamp',
                'ornamental_items': 'Ornamental Items',
                'ceiling_lamp': 'Ceiling Lamp',
                'floor_lamp': 'Floor Lamp'
            }
            
            # Convert URL categories to actual names
            category_names = []
            for cat in url_categories:
                # Check if it's in our mapping
                if cat.lower() in [k.lower() for k in slug_to_name.keys()]:
                    # Find the correct key (case-insensitive)
                    key = next(k for k in slug_to_name.keys() if k.lower() == cat.lower())
                    category_names.append(slug_to_name[key])
                else:
                    # Handle special cases
                    guessed_name = cat.replace('_', ' ').replace('-', ' ').title()
                    # Fix common acronyms
                    if 'tv' in cat.lower():
                        guessed_name = guessed_name.replace('Tv', 'TV')
                    category_names.append(guessed_name)
            
            print("DEBUG - Looking for categories:", category_names)
            
            # Filter products
            products = products.filter(category__name__in=category_names)
            
            # Get the actual Category objects
            categories = Category.objects.filter(name__in=category_names)
            
            print("DEBUG - Found categories:", list(categories.values_list('name', flat=True)))
            print("DEBUG - Product count:", products.count())
        # if 'category' in request.GET:
        #     url_categories = request.GET['category'].split(',')
        #     print("DEBUG - URL categories:", url_categories)
            
        #     # Map URL slugs to actual category names
        #     slug_to_name = {
        #         'sofa': 'Sofa',
        #         'tv_unit': 'TV Unit',
        #         'coffee_table': 'Coffee Table',
        #         'beds': 'Beds',
        #         'mattresses': 'Mattresses',
        #         'matressess': 'Mattresses',  # Handle typo
        #         'wardrobes': 'Wardrobes',
        #         'dining_tables': 'Dining Tables',
        #         'dinning_tables': 'Dining Tables',  # Handle typo
        #         'dining_chair': 'Dining Chair',
        #         'dinning_chair': 'Dining Chair',  # Handle typo
        #         'dining_set': 'Dining Set',
        #         'dinning_set': 'Dining Set',  # Handle typo
        #         'desk': 'Desk',
        #         'office_chair': 'Office Chair',
        #         'candles_and_holders': 'Candles and Holders',
        #         'throws_and_blankets': 'Throws and Blankets',
        #         'table_lamp': 'Table Lamp',
        #         'ornamental_items': 'Ornamental Items',
        #         'ceiling_lamp': 'Ceiling Lamp',
        #         'floor_lamp': 'Floor Lamp'
        #     }
            
        #     # Convert URL slugs to actual names
        #     category_names = []
        #     for slug in url_categories:
        #         if slug in slug_to_name:
        #             category_names.append(slug_to_name[slug])
        #         else:
        #             # Try to guess the name
        #             guessed_name = slug.replace('_', ' ').title()
        #             category_names.append(guessed_name)
            
        #     print("DEBUG - Looking for categories:", category_names)
            
        #     # Filter products
        #     products = products.filter(category__name__in=category_names)
            
        #     # Get the actual Category objects
        #     categories = Category.objects.filter(name__in=category_names)
            
        #     print("DEBUG - Found categories:", list(categories.values_list('name', flat=True)))
        #     print("DEBUG - Product count:", products.count())

        if 'q' in request.GET:
            query = request.GET['q']
            print("query ", query)
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            print("search results:", products.count())
    
    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)





def product_detail(request, product_id):
    print("product_id", product_id)
    productss = get_object_or_404(product, pk=product_id)

    context = {
        'product': productss,
    }

    return render(request, 'products/product_detail.html', context)
