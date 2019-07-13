from rest_framework.routers import DefaultRouter

from digital_backend.apps.criteria import views

router = DefaultRouter()
router.register('criterion', views.CriterionViewSet, basename='criterion')
