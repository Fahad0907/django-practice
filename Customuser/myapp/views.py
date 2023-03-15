from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RegisterSerializer,LoginSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from .models import Profile
import jwt
from django.conf import settings
# Create your views here.

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }
class Utli:
    @staticmethod
    def sendEmail(data):
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'],to=[data['to']])
        email.send()
        

class RegisterView(APIView):
    def post(self, request,format=None):
        serializer = RegisterSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_data = serializer.data
            user = Profile.objects.get(email= user_data['email'])
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            print(current_site)
            relative_link = reverse('email-verify')
            absurl = 'http://' + current_site + relative_link + "?token="+str(token)
            email_body = "Hi " + user.user_name + " verify your email \n" + absurl
            data = {'email_body' : email_body, 'email_subject' : "verify your email",'to' : user.email}
            Utli.sendEmail(data)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        return Response({"e":"request.user"})
    
class LoginView(APIView):
    def post(self, request,format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            e = Profile.objects.get(phone='01627174307')
            print(e)
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=e.email, password=password)
            print(user)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'msg' : "login failed"},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class EmailVerify(APIView):
    def get(self, request):
        data = request.query_params
        print(data['token'])
        try:
            payload = jwt.decode(str(data['token']), settings.SECRET_KEY, algorithms=['HS256'])
            user = Profile.objects.get(id=payload['user_id'])
            if not user.is_varified:
                user.is_varified = True
                user.save()
            return Response({"access_token" : str(data['token'])},status=status.HTTP_201_CREATED)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error' : 'Authentication expired'},status=status.HTTP_400_BAD_REQUEST)
        
