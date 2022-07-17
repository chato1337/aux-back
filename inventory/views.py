from inventory import serializers
from inventory.serializers import CreateProductSerializer, CreateSupplierSerializer, ProductSerializer, SupplierSerializer
from inventory.models import Product, Supplier
from inventory.services.inventory_service import InventoryService
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class GetView(APIView):
    def get(self, request):
        inventory_list = Product.objects.all()
        serializer = ProductSerializer(inventory_list, many=True)

        return Response(serializer.data)

class AddView(APIView):
    def post(self, request):

        serializer = CreateProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        return Response(ProductSerializer(product).data)

class GetSuppliersView(APIView):
    def get(self, request):
        supplier_list = Supplier.objects.all()

        serializer = SupplierSerializer(supplier_list, many=True)

        return Response(serializer.data)

class AddSupplierView(APIView):
    def post(self, request):
        serializer = CreateSupplierSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        supplier = serializer.save()

        return Response(SupplierSerializer(supplier).data)