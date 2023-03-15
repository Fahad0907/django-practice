from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import User,AnotherTable,Blog,Customer,Product
from .serializers import UserCreateSerializer,AnotherSerializer,BlogSerializer
from django.db.models import Count,Avg,Sum
# Create your views here.

class Register(APIView):
    def post(self,request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class AnotherList(APIView):
    def get(self,request):
        print(User.objects.get(username="fahad").id)
        query = AnotherTable.objects.all()
        serializer = AnotherSerializer(query,many=True)
        return Response(serializer.data)
    def post(self,request):
        print(User.objects.get(username="fahad"))
        serizliser = AnotherSerializer(data=request.data)
        if serizliser.is_valid():
            serizliser.save();
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class BlogList(APIView):
    def post(self,request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
#aggregate and annotate tesing
class Testing(APIView):
    def get(self,request):
        #agerage customer age
        # result = Customer.objects.aggregate(Sum('product__amount'))
        #specific persons amount in product
        # result = Customer.objects.filter(id=1).aggregate(Sum('product__amount'))
        #amount of product purchased by earch customer
        result = Product.objects.values('customer').annotate(Sum('amount'))
        print(result)
        return Response({"message" : "ok"})