from atexit import register
from django.urls import path,include
from .views import RegisterView,LoginView,EmailVerify

urlpatterns = [
   
    path('reg/',RegisterView.as_view(), name='reg'),
    path('log/',LoginView.as_view(), name='log'),
    path('email-verify/',EmailVerify.as_view(), name='email-verify'),
]
