from rest_framework import serializers

from digital_backend.apps.criteria.models import Criterion


class CriterionSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(source='machine_name')

    class Meta:
        model = Criterion
        fields = ('name', 'uuid', 'weight')
