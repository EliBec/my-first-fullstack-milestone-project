from django.contrib import admin
from .models import Product, Category, Subcategory


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'category',
        'subcategory',
        'name',
        'price',
        'image',
    )

   
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'active',
    )


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'active',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)

