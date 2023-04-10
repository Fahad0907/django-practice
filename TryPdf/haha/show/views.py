from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class ShowView(APIView):
    def get(self, request):
        print('ok')
        return Response(status=status.HTTP_200_OK)
