from django.db import models

# from typing import Union, List
# from django.db.models import QuerySet
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

    def save(self, *args, **kwargs):
        if not self.id:
            self.uuid = uuid_lib.uuid4()
        super(Sprint, self).save(*args, **kwargs)
