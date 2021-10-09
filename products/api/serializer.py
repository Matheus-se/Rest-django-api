from products.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    vendor = serializers.SerializerMethodField('get_vendor_from_product')
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'code', 'price', 'vendor']
        
    def get_vendor_from_product(self, product):
        vendor = product.vendor.username
        return vendor