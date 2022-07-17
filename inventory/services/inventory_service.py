from inventory.models import Product, Supplier

class InventoryService:
    def createInventory(data):
        newInventory = Product.objects.create(
            supplier=Supplier.objects.get(pk=data["supplier_id"]),
            name=data["name"],
            description="N/A",
            price=data["price"],
            # category=data["category"],
            stock=data["stock"],
            unit=data["unit"],
            expiration_date=data["expiration_date"],
            entry_date=data["entry_date"],
        )
        newInventory.save()
        return newInventory