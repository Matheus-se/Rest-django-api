from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework import authentication

class Vendor(AbstractUser):
    cnpj = models.CharField(max_length=14, unique=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    
    def __str__(self):
        return self.username

class BearerAuthentication(authentication.TokenAuthentication):
    keyword = 'Bearer'

@receiver(post_save, sender=Vendor)
def create_token(sender, instance=None, created=False, *args, **kwargs):
    if created:
        Token.objects.create(user=instance)