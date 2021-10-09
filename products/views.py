from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Product
from vendor.models import BearerAuthentication
from .api.serializer import ProductSerializer

@api_view(['GET', ])
@permission_classes(())
def get_product_view(request, id):
    
    try: 
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    authentication_classes = ()
    permission_classes = ()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'code', 'price', 'vendor__username', 'vendor__cnpj', 'vendor__email')

@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def update_product_view(request, id):
    
    try: 
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user = request.user
    if product.vendor != user:
        return Response({'error': "You don't have permission to edit this product"})
    
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['message'] = "product updated"
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE', ])
@permission_classes((IsAuthenticated,))
def delete_product_view(request, id):
    
    try: 
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user = request.user
    if product.vendor != user:
        return Response({'error': "You don't have permission to delete this product"})
    
    if request.method == 'DELETE':
        deleted = product.delete(); 
        data = {}
        if deleted:
            data['message'] = "product deleted"
            return Response(data=data, status=status.HTTP_200_OK)
        data['error'] = "Delete failed"
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def post_product_view(request):
    
    user = request.user
    
    product = Product(vendor=user)
    
    if request.method == 'POST':
        serializer = ProductSerializer(product, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

