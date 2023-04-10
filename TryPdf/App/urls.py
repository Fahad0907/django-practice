from django.urls import path
from .views import render_pdf_view,Show,TableView,TableApiView
urlpatterns = [
    path('',render_pdf_view,name='render-pdf'),
    path('show',Show.as_view(),name="show"),
    path('table/',TableView.as_view(), name="table"),
    path('table-api/', TableApiView.as_view(), name='table-api-view')
]
