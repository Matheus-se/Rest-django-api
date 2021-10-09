from django.urls import path
from . import views
from .views import ProductsListView
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'vendor'

urlpatterns = [
    path('register', views.register_vendor_view, name="vendor-post"),
    path('<id>/', views.list_vendor_view, name="vendor-get"),
    path('login', obtain_auth_token, name="login"),
    path('list', ProductsListView.as_view(), name="vendor-list"),
    path('account', views.vendor_account_view, name="vendor-account"),
    path('update', views.update_vendor_view, name="vendor-update"),
    path('delete', views.delete_vendor_view, name="vendor-delete"),
]
