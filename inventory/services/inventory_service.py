from inventory.models import Product

class InventoryService:
    def createInventory(data):
        newInventory = Product.objects.create(
            name=data["name"],
            category=data["category"],
            stock=data["stock"],
            unit=data["unit"]
        )
        newInventory.save()