from rest_framework.viewsets import ModelViewSet

from digital_backend.apps.criteria.models import Criterion
from digital_backend.apps.criteria.serializers import CriterionSerializer


class CriterionViewSet(ModelViewSet):
    serializer_class = CriterionSerializer
    queryset = Criterion.objects.all()
