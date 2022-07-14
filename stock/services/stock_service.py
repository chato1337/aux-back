from stock.models import Order
from inventory.models import Product

class StockService:
    def createStock(data):
        # newStock = Order.objects.create(
        #     inventory = Product.objects.get(pk=data['inventory_id']),
        #     sale_value = data["sale_value"],
        #     tax = data["tax"],
        #     initial_value = data["initial_value"]
        # )

        # newStock.save()
        pass