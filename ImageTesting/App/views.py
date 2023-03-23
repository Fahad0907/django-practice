from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ImageSerializer
from rest_framework import status
from django.core.files.storage import FileSystemStorage


# Create your views here.

class ImageView(APIView):
    def post(self, request):
     
        serializer = ImageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
def show(request):
    return render(request,'t.html')