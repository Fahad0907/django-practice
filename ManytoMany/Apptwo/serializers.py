from rest_framework import serializers
from .models import *

class Aserilizer(serializers.ModelSerializer):
    class Meta:
        model = A
        fields = '__all__'
        
class Bserilizer(serializers.ModelSerializer):
    class Meta:
        model = B
        fields = '__all__'
        
class Cserializer(serializers.ModelSerializer):
    # a_id = Aserilizer(many=False,read_only=True)
    # b_id = Bserilizer(many=False,read_only=True)
    
    class Meta:
        model = C
        fields = ['id','name','a_id','b_id']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        a_id = data['a_id']
        b_id = data['b_id']
        
        if a_id:
            a = A.objects.get(id=a_id)
            a_serializer = Aserilizer(a,many=False)
            data['a_id'] = a_serializer.data
        if b_id:
            b = B.objects.get(id=b_id)
            data['b_id'] = {
                'id' : b.id,
                'name' : b.name
            }
        return data
            
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneUser
        fields = ['name','age','phone_id']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        phone_id = data['phone_id']
        if phone_id:
            phone = Phone.objects.get(id=phone_id)
            data['phone_id'] = {
                "name" : phone.name,
                "price" : phone.price
            }
        return data


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name','location','p_user']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        p_user = data['p_user']
        if p_user:
            puser = PhoneUser.objects.get(id=p_user)
            pserializer = UserSerializer(puser,many=False)
            data['p_user'] = pserializer.data
        return data