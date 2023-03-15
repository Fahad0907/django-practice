from rest_framework import serializers
from .models import User,AnotherTable,Blog

class UserCreateSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(write_only = True, required = True)
    class Meta:
        model = User
        fields = ['email','password','first_name','last_name','username','re_password']
    def validate(self, attrs):
        if attrs['password'] != attrs['re_password']:
            print("not match")
            raise serializers.ValidationError('password didnt match')
        attrs.pop('re_password')
        return attrs
    def create(self, validateData):
        return User.objects.create_user(**validateData)
    
class AnotherSerializer(serializers.ModelSerializer):
    userdata= UserCreateSerializer(source='userr',read_only=True)
    class Meta:
        model = AnotherTable
        fields = '__all__'
        extra_kwargs = {'userr':{'write_only':True}}
        
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'