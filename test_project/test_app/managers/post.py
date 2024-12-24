from datetime import timezone, timedelta
from django.db.models import Value, F, CharField # field
from django.db.models.functions import Concat

from django.db.models import Manager, QuerySet


class PostQuerySet(QuerySet):
    def filter_created_yesterday(self):
        return self.filter(
            time_created_at=timezone.now() - timedelta(days=1)
        )

    def with_user_info(self):
        return self.annotate(
            user_info=Concat(F('user__username'), Value(' ('), F('user__email'), Value(')'), output_field=CharField())
        )


class PostManager(Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def filter_created_yesterday(self):
        return self.get_queryset().filter_created_yesterday()
