from typing import Tuple
from inventory.serializers import InventorySerializer
from inventory.models import Product
from inventory.services.inventory_service import InventoryService
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class GetView(APIView):
    def get(self, request):
        inventory_list = Product.objects.all()
        serializer = InventorySerializer(inventory_list, many=True)

        return Response(serializer.data)

class AddView(APIView):
    def post(self, request):

        InventoryService.createInventory(request.data)

        return Response("store added!")