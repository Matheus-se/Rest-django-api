from django.db import models

from vendor.models import Vendor

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)
    price = models.FloatField(null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="products")
    
    def __str__(self):
        return self.name