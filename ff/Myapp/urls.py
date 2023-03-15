from django.urls import path,include
from .views import RegisterView
urlpatterns = [
    path('reg/',RegisterView.as_view(), name="register")
]