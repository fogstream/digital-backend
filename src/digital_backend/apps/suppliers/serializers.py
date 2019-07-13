from django.db import models
from django.db.models import Avg, Case, When, F, Q, Count
from operator import itemgetter

from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from digital_backend.apps.criteria.models import Criterion
from digital_backend.apps.suppliers.models import Supplier, Vote


class SupplierCheckRequest(serializers.Serializer):  # noqa
    query = serializers.CharField(required=True)


class SupplierAssessment(serializers.Serializer):  # noqa
    criterion_uuid = serializers.UUIDField(required=True)
    inn = serializers.CharField(
        required=False, min_length=10, max_length=12
    )
    ogrn = serializers.CharField(
        required=False, min_length=13, max_length=13
    )
    score = serializers.FloatField(required=True)

    def validate(self, attrs):
        inn, ogrn = attrs.get('inn'), attrs.get('ogrn')
        if not inn and not ogrn:
            raise ValidationError(
                _('Required to have at least one field from: inn, ogrn')
            )
        return super().validate(attrs)


class CriteriaSerializer(serializers.Serializer):
    name = serializers.CharField()
    is_clean = serializers.BooleanField()


class SupplierSerializer(serializers.ModelSerializer):  # noqa
    name = serializers.CharField()
    inn = serializers.CharField()
    status = serializers.CharField()
    criteria = serializers.SerializerMethodField()
    percent = serializers.SerializerMethodField()

    class Meta:
        model = Supplier
        fields = '__all__'

    def criteria_qs(self, supplier):
        return Criterion.objects.filter(
            votes__supplier=supplier
        ).annotate(
            avg_score=Avg('votes__score')
        ).annotate(
            is_clean=Case(
                When(
                    Q(avg_score=F('votes__criterion__weight')),
                    then=True
                ),
                default=False,
                output_field=models.BooleanField()
            )
        ).values('name', 'is_clean')

    def get_criteria(self, obj):
        criteria = self.criteria_qs(obj)
        return CriteriaSerializer(criteria, many=True).data

    def get_percent(self, obj):
        criteria = self.criteria_qs(obj)
        total_count = criteria.count()
        counts = criteria.aggregate(
            count_clean=Count(
                'is_clean',
                filter=Q(is_clean=True)
            )
        )
        unclean = counts.get('count_clean') or 0

        return float(unclean / total_count * 100)


class SupplierCheckResultSerializer(SupplierSerializer):  # noqa
    criteria = serializers.SerializerMethodField()


class VoteSerializer(serializers.ModelSerializer):
    inn = serializers.CharField(source='supplier.inn')
    ogrn = serializers.CharField(source='supplier.ogrn')
    criterion_uuid = serializers.UUIDField(source='criterion.uuid')

    class Meta:
        model = Vote
        fields = ('inn', 'ogrn', 'criterion_uuid', 'score')
