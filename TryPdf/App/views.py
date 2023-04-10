from django.shortcuts import render,redirect
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Customer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
# Create your views here.
# def anotherView(request):
#     return render(request, 'tem.html')

class Show(TemplateView):
   template_name = 'Haha/hi.html'
   
def render_pdf_view(request):
    template_path = 'customer.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
 
class TableApiView(APIView):
   def get(self, request):
      query = Customer.objects.all()
      serializer = CustomerSerializer(query, many=True)
      return Response(serializer.data)
   
   
class TableView(TemplateView):
   template_name = 'tem.html'
   
   def get_context_data(self, **kwargs):
      context = super(TableView, self).get_context_data(**kwargs)
      query = Customer.objects.all()
      context.update({
         'customer' : query
      })
      return context