from django.urls import path
from .views import *
urlpatterns = [
    path('me',ShowView.as_view(), name="view")
]
