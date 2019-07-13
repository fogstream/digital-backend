from rest_framework.routers import DefaultRouter

from digital_backend.apps.suppliers import views

router = DefaultRouter()

router.register('suppliers', views.SupplierViewSet, basename='suppliers')
