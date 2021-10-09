from django.urls import path
from . import views
from .views import ProductsListView

app_name = 'product'

urlpatterns = [
    path('<id>/', views.get_product_view, name="product-get"),
    path('delete/<id>', views.delete_product_view, name="product-delete"),
    path('update/<id>', views.update_product_view, name="product-put"),
    path('add', views.post_product_view, name="product-post"),
    path('list', ProductsListView.as_view(), name="product-list"),
]
