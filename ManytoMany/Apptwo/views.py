from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from django.http import Http404
# Create your views here.

class CApiView(APIView):
    def get_object(self, id):
        try:
            return C.objects.get(id=id)
        except C.DoesNotExist:
            raise Http404
        
    def post(self, request):
        serializer = Cserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        query = C.objects.all()
        serializer = Cserializer(query,many=True)
        return Response(serializer.data)
    def put(self, request,id):
        c = self.get_object(id)
        serializer = Cserializer(c,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        
        

class CompanyView(APIView):
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        query = Company.objects.all()
        serializer = CompanySerializer(query,many=True)
        return Response(serializer.data)