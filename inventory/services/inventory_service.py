from inventory.models import Store


class InventoryService:
    def createInventory(data):
        newInventory = Store.objects.create(
            name=data["name"],
            category=data["category"],
            stock=data["stock"],
            unit=data["unit"]
        )
        newInventory.save()