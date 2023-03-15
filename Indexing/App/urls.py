
from django.urls import path
from .views import A,add,TryList,TryListT,a,Yahoo_list
urlpatterns = [
   
   
    path('a/',a,name="a"),
    path('add/',add,name="add"),
    path('try/',TryList.as_view(),name="try"),
    path('tryt/',TryListT.as_view(),name="tryt"),
    path('yahoo/<str:ticker>/',Yahoo_list.as_view(),name="tryt"),
]
