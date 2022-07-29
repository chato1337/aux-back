from django.shortcuts import render
from rest_framework.views import APIView
from inventory.models import Product
from inventory.serializers import CreateProductSerializer, ProductSerializer
from stock.models import Bill, Order
from stock.serializers import BillFlatSerializer, BillSerializer, CreateBillSerializer, CreateOrderSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
class GetBillView(generics.ListAPIView):
    serializer_class = BillSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('id',)
    ordering_fields = ('created_at', 'id',)

    def get_queryset(self):
        return Bill.objects.all()


class AddBillView(APIView):
    def post(self, request):
        total = 0

        #create new bill
        new_bill = {
            'customer': 1,
            'seller': 1,
            'payment_type': 'cash',
            'total': total
        }
        bill_serializer = CreateBillSerializer(data=new_bill)
        bill_serializer.is_valid(raise_exception=True)

        bill = bill_serializer.save()
        for item in request.data:
            #update stock for every product buyed in order
            product = Product.objects.get(pk=item['id'])
            product_dict = ProductSerializer(product).data

            less_quantity = product.stock - item['quantity']
            edit_product = {
                **product_dict,
                'stock': less_quantity,
                'category': product.category.id,
                'supplier': product.supplier.id
            }
            serializer = CreateProductSerializer(product, data=edit_product)
            serializer.is_valid(raise_exception=True)
            updated_product = serializer.save()
            total = total + item['subtotal']

            #create new order
            new_order = {
                'product': product.id,
                'bill': bill.id,
                'quantity': item['quantity'],
                'discount': 0,
                'total': item['subtotal'],
                'tax': 0
            }

            order_serializer = CreateOrderSerializer(data=new_order)
            order_serializer.is_valid(raise_exception=True)
            updated_order = order_serializer.save()

        #update bill with total price
        bill_dict = BillFlatSerializer(bill).data
        update_bill = { **bill_dict, 'total': total }
        total_bill_serializer = CreateBillSerializer(bill, data=update_bill)
        total_bill_serializer.is_valid(raise_exception=True)
        final_bill = total_bill_serializer.save()

        return Response(BillSerializer(final_bill).data)