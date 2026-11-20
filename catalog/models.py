from django.db import models
from django.contrib.auth.models import User

class Size(models.Model):
    label = models.CharField(max_length=50, unique=True)
    width_cm = models.IntegerField(null=True, blank=True)
    length_cm = models.IntegerField(null=True, blank=True)
    sort = models.IntegerField(default=0)

class Color(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hex = models.CharField(max_length=7, blank=True)

class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=100, unique=True, blank=True)
    material = models.CharField(max_length=200, blank=True)
    photo_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ProductVariant(models.Model):
    model = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="variants")
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    stock_qty = models.IntegerField()
    avg_cost = models.IntegerField()
    base_price = models.IntegerField()
    min_stock = models.IntegerField()
    is_active = models.BooleanField(default=True)

class ProductBarcode(models.Model):
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name="barcodes")
    barcode = models.CharField(max_length=100, unique=True)

class Purchase(models.Model):
    supplier = models.CharField(max_length=200, blank=True)
    doc_number = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.IntegerField()

class Sale(models.Model):
    number = models.CharField(max_length=100, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    payment_method = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    qty = models.IntegerField()
    base_price = models.IntegerField()
    price = models.IntegerField()
    cost_price = models.IntegerField()

class Return(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="returns")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class ReturnItem(models.Model):
    return_obj = models.ForeignKey(Return, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    qty = models.IntegerField()
    amount = models.IntegerField()

class WriteOff(models.Model):
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    qty = models.IntegerField()
    reason = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Inventory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class InventoryItem(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    qty_system = models.IntegerField()
    qty_fact = models.IntegerField()


class StockMovement(models.Model):
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name="movements")
    type = models.CharField(max_length=20)
    qty = models.IntegerField()
    ref_type = models.CharField(max_length=50, blank=True)
    ref_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, related_name="expenses")
    amount = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)