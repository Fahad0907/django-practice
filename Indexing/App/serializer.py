from rest_framework import serializers
from .models import yahoo,T,Tryindex
class ser(serializers.ModelSerializer):
    class Meta:
        model = yahoo
        fields = '__all__'
        
class serT(serializers.ModelSerializer):
    class Meta:
        model = T
        fields = '__all__'
        
class TrySr(serializers.ModelSerializer):
    class Meta:
        model = Tryindex
        fields = '__all__'