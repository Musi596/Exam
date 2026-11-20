from rest_framework.serializers import ModelSerializer
from .models import *


class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"


class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"


class ProductVariantSerializer(ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = "__all__"


class ProductBarcodeSerializer(ModelSerializer):
    class Meta:
        model = ProductBarcode
        fields = "__all__"


class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"


class PurchaseItemSerializer(ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = "__all__"


class SaleSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"


class SaleItemSerializer(ModelSerializer):
    class Meta:
        model = SaleItem
        fields = "__all__"


class ReturnSerializer(ModelSerializer):
    class Meta:
        model = Return
        fields = "__all__"


class ReturnItemSerializer(ModelSerializer):
    class Meta:
        model = ReturnItem
        fields = "__all__"


class WriteOffSerializer(ModelSerializer):
    class Meta:
        model = WriteOff
        fields = "__all__"


class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class InventoryItemSerializer(ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = "__all__"


class StockMovementSerializer(ModelSerializer):
    class Meta:
        model = StockMovement
        fields = "__all__"


class ExpenseCategorySerializer(ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = "__all__"


class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"