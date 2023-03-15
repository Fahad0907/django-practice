from .models import UserAccount
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserAccount
        fields = ['email', 'password','phone']
        extra_kwargs = {
                'password': {'write_only': True}
        }
    # def validate(self, attrs):
    #     username = attrs.get('user_name', '')
    #     if  len(username)<4:
    #         raise serializers.ValidationError('username should have atleast 4 digit')
    #     return attrs
    # def create(self, validate_data):
    #     return UserAccount.objects.create_user(**validate_data)