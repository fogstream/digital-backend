import re
from django.db.models import Q
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from digital_backend.apps.suppliers.models import Supplier
from digital_backend.apps.suppliers.serializers import (
    SupplierSerializer, SupplierCheckRequest, SupplierAssessment,
    VoteSerializer)
from digital_backend.apps.suppliers.utils import send_vote


class SupplierViewSet(ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

    @staticmethod
    def supplier_search(query):
        inn = re.search(r'(^\d{10}$)|(^\d{12}$)', query)
        inn = inn and inn.group()
        ogrn = re.search(r'(^\d{13}$)', query)
        ogrn = ogrn and ogrn.group()
        suppliers = Supplier.objects.all()
        if inn:
            supplier = get_object_or_404(suppliers, inn=inn)
        elif ogrn:
            supplier = get_object_or_404(suppliers, ogrn=ogrn)
        else:
            supplier = suppliers.filter(name__icontains=query).first()
            if not supplier:
                raise NotFound()
        return supplier

    @swagger_auto_schema(
        request_body=SupplierCheckRequest(),
        responses={200: SupplierSerializer()}
    )
    @action(methods=('post',), detail=False)
    def check(self, request):
        query_params = SupplierCheckRequest(data=request.data)
        query_params.is_valid(raise_exception=True)
        query = query_params.validated_data['query']
        supplier = self.supplier_search(query)
        return Response(SupplierSerializer(instance=supplier).data)

    @swagger_auto_schema(request_body=SupplierAssessment())
    @action(methods=('post',), detail=False)
    def vote(self, request):
        serializer = SupplierAssessment(data=request.data)
        serializer.is_valid(raise_exception=True)
        inn = serializer.validated_data.get('inn')
        ogrn = serializer.validated_data.get('ogrn')
        filters = Q()
        if inn:
            filters &= Q(inn=inn)
        if ogrn:
            filters &= Q(inn=inn)
        supplier = get_object_or_404(Supplier.objects.filter(filters))
        vote = send_vote(
            supplier=supplier,
            criterion_uuid=serializer.validated_data['criterion_uuid'],
            author=request.user,
            score=serializer.validated_data['score']
        )
        return Response(VoteSerializer(vote).data)
