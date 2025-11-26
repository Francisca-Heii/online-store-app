
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('store.urls')),
    path('products/', include('products.urls')), 
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),    
    path('review/', include('review.urls')),    
] 
# Always serve media files (for both development and production)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)