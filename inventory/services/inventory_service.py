from inventory.models import Category, Product, Supplier

class InventoryService:
    def createInventory(data):
        newInventory = Product.objects.create(
            supplier=Supplier.objects.get(pk=data["supplier_id"]),
            name=data["name"],
            description="N/A",
            price=data["price"],
            category=Category.objects.get(pk=data["category_id"]),
            stock=data["stock"],
            unit=data["unit"],
            expiration_date=data["expiration_date"],
            entry_date=data["entry_date"],
        )
        newInventory.save()
        return newInventory