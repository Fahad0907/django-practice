from django.urls import path
from .views import *
urlpatterns = [
    path('car', CarApiView.as_view(),name="car"),
    path('bucket', BucketApiView.as_view(),name="bucket"),
]
