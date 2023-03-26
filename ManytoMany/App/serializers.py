from rest_framework import serializers
from .models import Car, Bucket

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        
class BucketSerializer(serializers.ModelSerializer):
    car_list = CarSerializer(many=True,read_only = True)
    class Meta:
        model = Bucket
        fields = ['id','name','total_price','car_list']
        
        
       