from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
# Create your views here.

class CarApiView(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
 
class BucketApiView(APIView):
    def post(self, request):
        print(request.data)
        serializer = BucketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
    
    def get(self, request):
        query =  Bucket.objects.all()
        serializers = BucketSerializer(query,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)    