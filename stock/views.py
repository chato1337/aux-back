from django.shortcuts import render
from rest_framework.views import APIView
from inventory.models import Product
from inventory.serializers import CreateProductSerializer, ProductSerializer
from stock.models import Invoice, Order
from stock.serializers import InvoiceFlatSerializer, InvoiceSerializer, CreateInvoiceSerializer, CreateOrderSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
class GetInvoiceView(generics.ListAPIView):
    serializer_class = InvoiceSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('id',)
    ordering_fields = ('created_at', 'id', 'total', 'customer')

    def get_queryset(self):
        return Invoice.objects.all()


class AddInvoiceView(APIView):
    def post(self, request):
        total = 0

        #create new bill
        new_invoice = {
            'customer': request.data['customer'],
            'seller': request.data['seller'],
            'payment_type': request.data['payment_type'],
            'total': request.data['total']
        }
        invoice_serializer = CreateInvoiceSerializer(data=new_invoice)
        invoice_serializer.is_valid(raise_exception=True)
        invoice = invoice_serializer.save()

        for item in request.data['products']:
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
                'invoice': invoice.id,
                'quantity': item['quantity'],
                'discount': 0,
                'total': item['subtotal'],
                'tax': 0
            }

            order_serializer = CreateOrderSerializer(data=new_order)
            order_serializer.is_valid(raise_exception=True)
            updated_order = order_serializer.save()

        #update invoice with total price
        invoice_dict = InvoiceFlatSerializer(invoice).data
        update_invoice = { **invoice_dict, 'total': total }
        total_invoice_serializer = CreateInvoiceSerializer(invoice, data=update_invoice)
        total_invoice_serializer.is_valid(raise_exception=True)
        final_invoice = total_invoice_serializer.save()

        return Response(InvoiceSerializer(final_invoice).data)