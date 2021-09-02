from django.db import models
from django.db.models import fields
from app.models import Customer, Product,Cart,OrederPlaced
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','name','locality','city','zipcode','state']