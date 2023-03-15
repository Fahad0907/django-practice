from django.urls import path
from .views import *
urlpatterns = [
    path("reg",Register.as_view(),name="reg"),
    path("another",AnotherList.as_view(),name="ano"),
    path("blog",BlogList.as_view(),name="blog"),
    path("ann",Testing.as_view(),name="test"),
]
