from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from digital_backend.apps.suppliers.enums import SupplierStatus


class SupplierType(models.Model):
    """Supplier type model."""

    name = models.CharField(max_length=256)
    criteria = models.ManyToManyField('criteria.Criterion', blank=True)

    class Meta:
        verbose_name = _('supplier type')
        verbose_name_plural = _('suppliers types')

    def __str__(self):
        return self.name


class Supplier(models.Model):
    """Supplier model."""
    name = models.CharField(max_length=256)
    inn = models.CharField(max_length=12, unique=True)
    ogrn = models.CharField(max_length=13, unique=True)
    type = models.ForeignKey(SupplierType, on_delete=models.PROTECT)  # noqa
    status = models.CharField(
        choices=SupplierStatus.choices(),
        default=SupplierStatus.RESEARCH,
        max_length=64
    )

    class Meta:
        verbose_name = _('supplier')
        verbose_name_plural = _('suppliers')

    def __str__(self):
        return self.name


class Tender(models.Model):
    """Tender model."""

    code = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    winner = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, null=True, blank=True,
        related_name='win_tenders',
    )
    buyer = models.ForeignKey(
        Supplier, on_delete=models.CASCADE,
        verbose_name=_('buyer'),
        null=True,
        related_name='tenders',
    )

    class Meta:
        verbose_name = _('tender')
        verbose_name_plural = _('tenders')

    def __str__(self):
        return self.name


class TenderMember(models.Model):
    """Tender member model."""
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    tender = models.ForeignKey(
        Tender, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _('tender member')
        verbose_name_plural = _('tender members')

    def __str__(self):
        return self.supplier.name


class Vote(models.Model):
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE)
    criterion = models.ForeignKey(
        'criteria.Criterion',
        on_delete=models.CASCADE,
        related_name='votes')
    score = models.FloatField()
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _('check result')
        verbose_name_plural = _('check results')
        unique_together = ('supplier', 'criterion')

    def clean(self):
        if self.score > self.criterion.weight:
            raise ValidationError(
                _('score can not be greater criterion weight')
            )
