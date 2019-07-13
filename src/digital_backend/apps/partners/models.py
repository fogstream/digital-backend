from django.db import models
from django.utils.translation import gettext as _


class PartnerType(models.Model):
    criteria = models.ManyToManyField('criteria.Criterion')

    class Meta:
        verbose_name = _('partner type')
        verbose_name_plural = _('partner types')


class Partner(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    type = models.ForeignKey(PartnerType, on_delete=models.CASCADE)
    api_endpoint = models.URLField()

    class Meta:
        verbose_name = _('partner')
        verbose_name_plural = _('partners')
