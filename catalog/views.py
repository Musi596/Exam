from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class SizeViewSet(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = ProductModel.objects.prefetch_related("variants")
    serializer_class = ProductModelSerializer


class ProductVariantViewSet(ModelViewSet):
    queryset = ProductVariant.objects.select_related("model", "size", "color").prefetch_related("barcodes")
    serializer_class = ProductVariantSerializer


class ProductBarcodeViewSet(ModelViewSet):
    queryset = ProductBarcode.objects.select_related("variant")
    serializer_class = ProductBarcodeSerializer


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.select_related("user").prefetch_related("items")
    serializer_class = PurchaseSerializer


class PurchaseItemViewSet(ModelViewSet):
    queryset = PurchaseItem.objects.select_related("purchase", "variant")
    serializer_class = PurchaseItemSerializer


class SaleViewSet(ModelViewSet):
    queryset = Sale.objects.select_related("user").prefetch_related("items", "returns")
    serializer_class = SaleSerializer


class SaleItemViewSet(ModelViewSet):
    queryset = SaleItem.objects.select_related("sale", "variant")
    serializer_class = SaleItemSerializer


class ReturnViewSet(ModelViewSet):
    queryset = Return.objects.select_related("sale", "user").prefetch_related("items")
    serializer_class = ReturnSerializer


class ReturnItemViewSet(ModelViewSet):
    queryset = ReturnItem.objects.select_related("return_obj", "variant")
    serializer_class = ReturnItemSerializer


class WriteOffViewSet(ModelViewSet):
    queryset = WriteOff.objects.select_related("variant", "user")
    serializer_class = WriteOffSerializer


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.select_related("user").prefetch_related("items")
    serializer_class = InventorySerializer


class InventoryItemViewSet(ModelViewSet):
    queryset = InventoryItem.objects.select_related("inventory", "variant")
    serializer_class = InventoryItemSerializer


class StockMovementViewSet(ModelViewSet):
    queryset = StockMovement.objects.select_related("variant", "user")
    serializer_class = StockMovementSerializer


class ExpenseCategoryViewSet(ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.select_related("category", "user")
    serializer_class = ExpenseSerializer
