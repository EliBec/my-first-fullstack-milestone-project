from django.urls import path
from . import views  # . means current directory

urlpatterns = [
    path('', views.display_all_products, name='products'),
    path('<int:product_id>', views.display_product_detail,
         name='display_product_detail'),
    path('category/<category_name>', views.products_by_category,
         name='products_by_category'),
    path('category/subcategory/<category_name>', views.products_by_category,
         name='products_by_subcategory'),
    path('addproduct/', views.add_product,
         name='add_product'),
    path('editproduct/<int:product_id>', views.edit_product,
         name='edit_product'),
    path('deleteproduct/<int:product_id>', views.delete_product,
         name='delete_product'),
    path('add_rating/<int:product_id>/', views.add_rating,
         name='add_rating'),
    path('edit_rating/<int:product_id>', views.edit_rating,
         name='edit_rating'),
    path('delete_rating/<int:product_id>', views.delete_rating,
         name='delete_rating'),
]
