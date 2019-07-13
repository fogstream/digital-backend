from django.db import models
from django.utils.translation import gettext as _


class ClientType(models.Model):
    criteria = models.ManyToManyField('criteria.Criterion')

    class Meta:
        verbose_name = _('client type')
        verbose_name_plural = _('clients types')


class Client(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')

