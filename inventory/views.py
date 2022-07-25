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
    serializer_class = SupplierSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'unit', 'entry_date', 'pk')

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset
        

class AddView(APIView):
    def post(self, request):
        serializer = CreateProductSerializer(data=request.data)
        serializer.is_valid()
        product = serializer.save()

        return Response(ProductSerializer(product).data)

class GetSuppliersView(generics.ListAPIView):
    serializer_class = SupplierSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'identifier', 'phone', 'email', 'pk', )

    def get_queryset(self):
        queryset = Supplier.objects.all()
        return queryset


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
    ordering_fields = ('name',)
    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

class EditCategoryView(APIView):
    def put(self, request):
        category = Category.objects.get(pk=request.data['id'])
        serializer = CreateCategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_category = serializer.save()

        return Response(CategorySerializer(updated_category).data)