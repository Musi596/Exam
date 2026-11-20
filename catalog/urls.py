from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("sizes", SizeViewSet)
router.register("colors", ColorViewSet)
router.register("product-models", ProductModelViewSet)
router.register("product-variants", ProductVariantViewSet)
router.register("product-barcodes", ProductBarcodeViewSet)
router.register("purchases", PurchaseViewSet)
router.register("purchase-items", PurchaseItemViewSet)
router.register("sales", SaleViewSet)
router.register("sale-items", SaleItemViewSet)
router.register("returns", ReturnViewSet)
router.register("return-items", ReturnItemViewSet)
router.register("write-offs", WriteOffViewSet)
router.register("inventories", InventoryViewSet)
router.register("inventory-items", InventoryItemViewSet)
router.register("stock-movements", StockMovementViewSet)
router.register("expense-categories", ExpenseCategoryViewSet)
router.register("expenses", ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
