from django.urls import path
from .views import *
urlpatterns = [
    path('c',CApiView.as_view(),name='c'),
    path('c/<int:id>',CApiView.as_view(),name='c-id'),
    path('company',CompanyView.as_view(),name="company")
]
