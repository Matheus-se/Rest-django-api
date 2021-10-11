from rest_framework import serializers
from products.api.serializer import ProductSerializer
from products.models import Product
from vendor.models import Vendor

class VendorSerializer(serializers.ModelSerializer):    
    
    products = ProductSerializer(many=True)
    
    class Meta:
        model = Vendor
        fields = ['id', 'username', 'email', 'password', 'cnpj', 'city', 'products']
        extra_kwargs = {
            'password': {'write_only': True}
        }


    #Needed for hash the password
    def create(self, validated_data):
        user = Vendor(
            email=validated_data['email'],
            username=validated_data['username'],
            cnpj=validated_data['cnpj'],
            city=validated_data['city'],
        )
        user.set_password(validated_data['password'])
        user.save()
        
        product_data = validated_data.pop('products')
        for product in product_data:
            Product.objects.create(vendor = user, **product)
        
        return user
    
class AccountSerializer(serializers.ModelSerializer):    
        
    class Meta:
        model = Vendor
        fields = ['id', 'username', 'email', 'cnpj', 'city']