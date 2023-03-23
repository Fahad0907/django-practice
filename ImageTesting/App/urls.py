from django.urls import path
from .views import *
urlpatterns = [
   path('',ImageView.as_view(),name="view"),
   path('show',show,name="show")
]