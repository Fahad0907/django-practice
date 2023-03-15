from unittest import result
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import yahoo,T,Tryindex
from .serializer import ser, serT,TrySr
from rest_framework.pagination import LimitOffsetPagination
from .paginate import Mypage
import json
import time
from .insert import yahoo_history_data_insert
# Create your views here.

def a(request):
    yahoo_history_data_insert()
    return HttpResponse('done')
class A(APIView,LimitOffsetPagination):
    def get(self, request, format=None):
        query = T.objects.all()
        results = self.paginate_queryset(query, request, view=self)
        serializer = serT(results, many=True, context={'request':request})
        mainList = []
        for i in range(len(serializer.data)):
            basic = {}
            basic['full name'] = serializer.data[i]['name']
            basic['full id'] = serializer.data[i]['id']
            mainList.append(basic)
        a  = self.get_paginated_response(mainList)
        return a
# class InsertData(APIView, Mypage):
#     def get(self, request):
#         queryset = yahoo_history.objects.all()
        
#         results =self.paginate_queryset(queryset, request)
#         serializer = ser(results, many=True)
        
#         return  Response({'links': {
#                 'next': self.get_next_link(),
#                 'previous': self.get_previous_link()
#                 },  
#                 'count': self.page.paginator.count,
#                 'results' : serializer.data
#         })


# class InsertData(APIView,LimitOffsetPagination):
#     def get(self, request, format=None):
#         starttime = time.time()
#         query = yahoo_history.objects.filter(ticker__contains='AAPL')
#         results = self.paginate_queryset(query, request, view=self)
#         serializer = ser(results, many=True, context={'request':request})
#         endtime = time.time()
#         print(endtime - starttime)
#         return self.get_paginated_response(serializer.data)

# class A(APIView, Mypage):
#     def get(self, request):
#         queryset = yahoo_history.objects.all()
        
#         results =self.paginate_queryset(queryset, request)
#         serializer = ser(results, many=True)
        
#         return  Response({'links': {
#             'next': self.get_next_link(),
#             'previous': self.get_previous_link()
#             },  
#             'results' : serializer.data
#         })
def add(request):
    for i in range(10000000):
        st_name = fake.name()
        for j in range(5):
            
            a = Tryindex.objects.create(
                name = st_name,
                email = str(j) + '@gmail.com',
                phone = '01627174307'
            )
            a.save()
    return HttpResponse('done')
class TryList(APIView,LimitOffsetPagination):
    def get(self, request):
        starttime = time.time()
        query = Tryindex.objects.filter(email='4@gmail.com')
        results = self.paginate_queryset(query, request, view=self)
        serializer = TrySr(results, many=True, context={'request':request})
        endtime = time.time()
        print(endtime - starttime)
        return self.get_paginated_response(serializer.data)
    

class TryListT(APIView,LimitOffsetPagination):
    def get(self, request):
        starttime = time.time()
        name = '4@gmail.com'
        #query = Tryindex.objects.raw('SELECT * FROM app_tryindex WHERE email = %s', [name])
        query = Tryindex.objects.filter(name='Fahad')
        results =self.paginate_queryset(query, request)
        serializer = TrySr(results, many=True)
        mainList = []
        for i in range(len(serializer.data)):
            show = {}
            show['full name'] = serializer.data[i]['name']
            show['full email'] = serializer.data[i]['email']
            show['phone no'] = serializer.data[i]['phone']
            mainList.append(show)
        endtime = time.time()
        print(endtime - starttime)
        return  Response({
            'links': 
            {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },  
            'results' : mainList
        })
        
class Yahoo_list(APIView,LimitOffsetPagination):
    def get(self, request,ticker):
        starttime = time.time()
        get_data = request.query_params
        query = ''
        try:
            if len(get_data)>=2:
                if 'date_start' in get_data and 'date_end' in get_data:
                    query = yahoo.objects.filter(ticker=ticker,date__gte = get_data['date_start'],date__lte = get_data['date_end'])
                else:
                    query = yahoo.objects.filter(ticker=ticker)
            else:
                query = yahoo.objects.filter(ticker=ticker)
        except:
            return Response({"status":{"code" :status.HTTP_500_INTERNAL_SERVER_ERROR , "message" : "date not valid" ,"details" : ""}  })
        else:
            results =self.paginate_queryset(query, request)
            serializer = ser(results, many=True)
            if len(serializer.data)>0:
                mainList = []
                for i in range(len(serializer.data)):
                    basic = {}
                    dailyStock = {}
                    dailyStockData = {}
                    output = {}
                    basic['ticker'] = serializer.data[i]['ticker']
                    dailyStock['date'] = serializer.data[i]['date']
                    dailyStock['open'] = serializer.data[i]['Open']
                    dailyStock['high'] = serializer.data[i]['High']
                    dailyStock['low'] = serializer.data[i]['Low']
                    dailyStock['close'] = serializer.data[i]['Close']
                    dailyStock['volume'] = serializer.data[i]['Volume']
                    dailyStock['split'] = serializer.data[i]['StockSplits']
                    dailyStock['dividend'] = serializer.data[i]['Dividends']
                    dailyStockData['daily_stock_data'] = dailyStock
                    output['basics'] = basic
                    output['output'] = dailyStockData
                    mainList.append(output)
                endtime = time.time()
                print(endtime - starttime)
                return  Response({
                    'links': 
                    {
                        'count': query.count(),
                        'next': self.get_next_link(),
                        'previous': self.get_previous_link()
                    },  
                    'results' : mainList
                })
            else:
                return Response({"status":{"code" :status.HTTP_404_NOT_FOUND , "message" : "Not found" ,"details" : ""}  })
            
            
#class HistoricalCandlestickDataList(APIView,LimitOffsetPagination):