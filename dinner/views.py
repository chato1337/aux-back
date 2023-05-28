from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from dinner.models import DinnerOrder, DinnerProduct, Table
from dinner.serializers import CreateDinnerOrderSerializer, CreateTableSerializer, DinnerOrderSelializer, DinnerProductSerializer, TableSerializer
from rest_framework.response import Response

# Create your views here.
class OrderListCreateView(APIView):
    def post(self, request):
        serializer = CreateDinnerOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        record = serializer.save()

        return Response(DinnerOrderSelializer(record).data)

    def get(self, request):
        order_id = request.query_params.get('id')
        if(order_id):
            return Response(
                DinnerOrderSelializer(DinnerOrder.objects.filter(pk=order_id), many=True).data
            )
        queryset = DinnerOrder.objects.all()
        return Response(DinnerOrderSelializer(queryset, many=True).data)

class TableListCreateView(APIView):
    def post(self, request):
        serializer = CreateTableSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        record = serializer.save()

        return Response(TableSerializer(record).data)

    def get(self, request):
        table_number = request.query_params.get('id')
        if table_number:
            return Response(
                TableSerializer(Table.objects.filter(number=table_number), many=True).data
            )
        return Response(TableSerializer(Table.objects.all(), many=True).data)

class TableUpdateView(generics.UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = CreateTableSerializer

class DinnerProductView(generics.ListCreateAPIView):
    queryset = DinnerProduct.objects.all()
    serializer_class = DinnerProductSerializer