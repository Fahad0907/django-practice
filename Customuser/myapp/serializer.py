from pyexpat import model
from rest_framework import serializers
from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['email', 'user_name', 'password','phone']
        extra_kwargs = {
                'password': {'write_only': True}
        }
    def validate(self, attrs):
        username = attrs.get('user_name', '')
        if  len(username)<4:
            raise serializers.ValidationError('username should have atleast 4 digit')
        return attrs
    def create(self, validate_data):
        return Profile.objects.create_user(**validate_data)
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model=Profile
        fields = ['email','password']