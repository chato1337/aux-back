from unicodedata import category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from inventory.models import Category, Product, Supplier
from inventory.serializers import (
    CategorySerializer,
    CreateCategorySerializer,
    CreateProductSerializer,
    CreateSupplierSerializer,
    ProductSerializer,
    SupplierSerializer
)

# Create your views here.
class GetView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'unit', 'entry_date', 'id', 'category')

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset


class AddView(APIView):
    def post(self, request):
        new_product = { **request.data, 'supplier': request.data['supplier_id'], 'category': request.data['category_id'] }
        serializer = CreateProductSerializer(data=new_product)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        return Response(ProductSerializer(product).data)

class EditView(APIView):
    def put(self, request):
        product = Product.objects.get(pk=request.data['id'])
        edit_product = { **request.data, 'supplier': request.data['supplier_id'], 'category': request.data['category_id'] }
        serializer = CreateProductSerializer(product, data=edit_product)
        serializer.is_valid(raise_exception=True)
        updated_product = serializer.save()

        return Response(ProductSerializer(updated_product).data)

class GetSuppliersView(generics.ListAPIView):
    serializer_class = SupplierSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'identifier', 'phone', 'email', 'id', )

    def get_queryset(self):
        queryset = Supplier.objects.all()
        return queryset

class GetFullSuppliersView(APIView):
    def get(self, request):
        supplier_list = Supplier.objects.all()

        return Response(SupplierSerializer(supplier_list, many=True).data)


class AddSupplierView(APIView):
    def post(self, request):
        serializer = CreateSupplierSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        supplier = serializer.save()

        return Response(SupplierSerializer(supplier).data)

class EditSupplierView(APIView):
    def put(self, request):
        supplier = Supplier.objects.get(pk=request.data['id'])
        serializer = CreateSupplierSerializer(supplier, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_supplier = serializer.save()

        return Response(SupplierSerializer(updated_supplier).data)

class AddCategoryView(APIView):
    def post(self, request):
        serializer = CreateCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = serializer.save()

        return Response(CategorySerializer(category).data)

class GetCategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'id', 'description',)
    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

class GetFullCategoryView(APIView):
    def get(self, request):
        category_list = Category.objects.all()

        return Response(CategorySerializer(category_list, many=True).data)

class EditCategoryView(APIView):
    def put(self, request):
        category = Category.objects.get(pk=request.data['id'])
        serializer = CreateCategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_category = serializer.save()

        return Response(CategorySerializer(updated_category).data)