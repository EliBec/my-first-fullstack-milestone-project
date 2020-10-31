from django.contrib import admin
from .models import Product, Category, Subcategory, Rating


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


class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'customer',
        'nickname',
        'rating',
        'headline',
        'comment',
        'recommend',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Rating, RatingAdmin)


