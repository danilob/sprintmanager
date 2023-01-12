from django.db import models

# from typing import Union, List
import uuid as uuid_lib

from apps.category.models import Category


class Issue(models.Model):

    sprint = models.ForeignKey(
        'sprint.Sprint',
        on_delete=models.SET_NULL,
        null=True,
    )
    categories = models.ManyToManyField(
        Category,
        related_name="issue_categories",
        blank=False,
    )
    level = models.ForeignKey(
        'level.Level',
        on_delete=models.SET_NULL,
        null=True,
    )

    dependencies = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
    )

    TODO = 'TD'
    DOING = 'DG'
    REVIEW = 'RW'
    DONE = 'DN'
    KANBAN = (
        (TODO, 'Aguardando'),
        (DOING, 'Em produção'),
        (REVIEW, 'Em Revisão'),
        (DONE, 'Concluído'),
    )
    description = models.CharField(max_length=200)
    begin_date = models.DateField(null=True, blank=True)
    forecast_date = models.DateField(null=True, blank=True)
    finished_date = models.DateField(null=True, blank=True)
    url = models.URLField(blank=True)
    uuid = models.UUIDField(
        db_index=True, default=uuid_lib.uuid4, unique=True, editable=False
    )
    status = models.CharField(choices=KANBAN, max_length=2, default=TODO)

    class Meta:
        verbose_name = 'Issue'
        verbose_name_plural = 'Issues'
        ordering = ['begin_date', 'description']

    def __str__(self):
        return self.description

    # def how_many_issues(self) -> int:
    #     pass

    # def issues(self) -> Union[QuerySet, List[Issue]]:
    #     pass

    # @property
    # def has_finished(self) -> bool:
    #     pass

    def save(self, *args, **kwargs):
        if not self.id:
            self.uuid = uuid_lib.uuid4()
        super(Issue, self).save(*args, **kwargs)
