from django.db import models

from typing import Union, List
from django.db.models import QuerySet
import uuid as uuid_lib


class Sprint(models.Model):
    description = models.CharField(max_length=200)
    begin_date = models.DateField(null=True, blank=True)
    forecast_date = models.DateField(null=True, blank=True)
    finished_date = models.DateField(null=True, blank=True)
    url = models.URLField(blank=True)
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        unique=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'Sprint'
        verbose_name_plural = 'Sprints'
        ordering = ['begin_date', 'description']

    def __str__(self):
        return self.description

    def how_many_issues(self) -> int:
        return self.issue_set.count()

    # def issues(self) -> Union[QuerySet, List['Issue']]:
    #     pass

    @property
    def has_finished(self) -> bool:
        from apps.issue.models import Issue

        issues = self.issue_set.all()
        if issues.count() > 0:
            if issues.exclude(status=Issue.DONE).exists():
                return False
            return True
        return False

    def is_sprint_delivered_late(self) -> bool:
        return (
            self.finished_date > self.forecast_date if (self.finished_date) else None
        )

    @staticmethod
    def sprint_delivered_late() -> Union[QuerySet, List['Sprint']]:
        from django.db.models import F
        from django.db.models.lookups import GreaterThan

        return (
            Sprint.objects.filter(finished_date__isnull=False)
            .annotate(
                is_late=GreaterThan(
                    F('finished_date') - F('begin_date'),
                    F('forecast_date') - F('begin_date'),
                )
            )
            .filter(is_late=True)
        )

    @property
    def complexity_level(self) -> int:
        from django.db.models import Sum

        Sprint.objects.annotate(
            _level_complexity_sum=Sum("issue__level__number_level"),
        )
        return Sprint.objects.filter(uuid=self.uuid).aggregate(
            sum_level=Sum('issue__level__number_level')
        )['sum_level']

    def sumarize_categories_count(self) -> list:
        from django.db.models import F, Count

        # Sprint.objects.values(
        #     'description', 'issue__categories__description'
        # ).annotate(qtde=Count('issue__categories__description'))
        return (
            Sprint.objects.annotate(category=F('issue__categories__description'))
            .values('category')
            .annotate(qtde=Count('issue__categories__description'))
            .filter(uuid=self.uuid)
        )

    def save(self, *args, **kwargs):
        if not self.id:
            self.uuid = uuid_lib.uuid4()
        super(Sprint, self).save(*args, **kwargs)
