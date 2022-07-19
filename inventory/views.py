from inventory import serializers
from inventory.serializers import CategorySerializer, CreateCategorySerializer, CreateProductSerializer, CreateSupplierSerializer, ProductSerializer, SupplierSerializer
from inventory.models import Category, Product, Supplier
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
        # print(request.data)
        # serializer = CreateProductSerializer(data=request.data)
        # serializer.is_valid()
        # product = serializer.save()

        # return Response(ProductSerializer(product).data)
        return Response(
            ProductSerializer(InventoryService.createInventory(request.data)).data
        )

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

class AddCategoryView(APIView):
    def post(self, request):
        serializer = CreateCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = serializer.save()

        return Response(CategorySerializer(category).data)
class GetCategoryView(APIView):
    def get(self, request):
        category_list = Category.objects.all()

        serializer = CategorySerializer(category_list, many=True)

        return Response(serializer.data)

class EditCategoryView(APIView):
    def put(self, request):
        category = Category.objects.get(pk=request.data['id'])
        serializer = CreateCategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_category = serializer.save()

        return Response(CategorySerializer(updated_category).data)