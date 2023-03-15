from django.urls import path,include
from .views import UserRegistrationView,UserLoginView

urlpatterns = [
   
    path('reg/',UserRegistrationView.as_view(), name='reg'),
    path('log/',UserLoginView.as_view(), name='log'),
]