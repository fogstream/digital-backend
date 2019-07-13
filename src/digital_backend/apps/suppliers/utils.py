from django.contrib.auth.models import User
from uuid import uuid4

from digital_backend.apps.criteria.models import Criterion
from digital_backend.apps.suppliers.models import Supplier, Vote


def send_vote(supplier: Supplier, criterion_uuid: uuid4,
              score: float, author: User):
    criterion = Criterion.objects.get(uuid=criterion_uuid)
    vote, _ = Vote.objects.update_or_create(
        author=author,
        criterion=criterion,
        supplier=supplier,
        defaults={"score": score})
    return vote
