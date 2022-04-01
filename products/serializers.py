from rest_framework import serializers
from .models import Product



#dat
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','price','inventory_quanity']