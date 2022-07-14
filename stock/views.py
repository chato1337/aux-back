from django.shortcuts import render
from rest_framework.views import APIView
from stock.models import Order
from stock.serializers import StockSerializer
from stock.services.stock_service import StockService
from rest_framework.response import Response

# Create your views here.
class GetView(APIView):
    def get(self, request):
        stock_list = Order.objects.all()
        
        serializer = StockSerializer(stock_list, many=True)

        return Response(serializer.data)

class AddView(APIView):
    def post(self, request):
        StockService.createStock(request.data)

        return Response("Stock added")