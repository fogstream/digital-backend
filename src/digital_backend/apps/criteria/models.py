import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Criterion(models.Model):
    """Criterion model"""

    name = models.CharField(max_length=256)
    uuid = models.UUIDField(
        max_length=256,
        unique=True,
        default=uuid.uuid4,
        editable=True
    )
    weight = models.FloatField(default=1)

    class Meta:
        verbose_name = _('criterion')
        verbose_name_plural = _('criteria')

    def __str__(self):
        return self.name

