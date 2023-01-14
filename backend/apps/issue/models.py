from django.db import models
from django.db.models import QuerySet
from typing import Union, List
import uuid as uuid_lib

from apps.category.models import Category
from apps.level.models import Level


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

    def how_many_categories(self) -> int:
        return self.categories.count()

    def name_categories(self) -> Union[QuerySet, List[str]]:
        return self.categories.values_list('description', flat=True)

    @staticmethod
    def issues_by_level(level: Level) -> Union[QuerySet, List['Issue']]:
        # return Issue.objects.filter(level=level)
        return level.issue_set.all()

    @staticmethod
    def issues_by_category(
        category: Category,
    ) -> Union[QuerySet, List['Issue']]:
        # return Issue.objects.filter(categories__in=[category])
        return category.issue_categories.all()

    @staticmethod
    def issues_with_some_of_two_specific_categories(
        first_category: Category, second_category: Category
    ) -> Union[QuerySet, List['Issue']]:
        from django.db.models import Q

        # Issue.objects.filter(
        #     ~(~Q(categories=first_category) & ~Q(categories=second_category))
        # )
        return Issue.objects.filter(
            Q(categories=first_category) | Q(categories=second_category)
        )

    @staticmethod
    def issues_with_two_specific_categories(
        first_category: Category, second_category: Category
    ) -> Union[QuerySet, List['Issue']]:
        from django.db.models import Q

        return Issue.objects.filter(Q(categories=first_category)).filter(
            Q(categories=second_category)
        )

    @staticmethod
    def issues_classified_by_max_duration() -> Union[QuerySet, List['Issue']]:
        from django.db.models import F

        return (
            Issue.objects.filter(status=Issue.DONE)
            .annotate(diff_date=F('finished_date') - F('begin_date'))
            .order_by('-diff_date')
        )

    @property
    def was_late(self) -> bool:
        return (
            (self.finished_date - self.begin_date)
            > (self.forecast_date - self.begin_date)
            if (self.finished_date and self.status == Issue.DONE)
            else None
        )

    @staticmethod
    def issue_concluded_late() -> Union[QuerySet, List['Issue']]:
        from django.db.models import F
        from django.db.models.lookups import GreaterThan

        return (
            Issue.objects.filter(status=Issue.DONE, finished_date__isnull=False)
            .annotate(
                is_late=GreaterThan(
                    F('finished_date') - F('begin_date'),
                    F('forecast_date') - F('begin_date'),
                )
            )
            .filter(is_late=True)
        )

    def save(self, *args, **kwargs):
        if not self.id:
            self.uuid = uuid_lib.uuid4()
        super(Issue, self).save(*args, **kwargs)
