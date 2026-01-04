from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import product, Category


class ProductAdmin(ImportExportModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    ordering = ('sku',)
    search_fields = ('name', 'sku')
    list_filter = ('category',)


class CategoryAdmin(ImportExportModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    search_fields = ('name',)


admin.site.register(product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
