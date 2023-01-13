from django.db import models

# from typing import Union, List
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

    # def how_many_categories(self) -> int:
    #     pass

    # def name_categories(self) -> Union[QuerySet, List[str]]:
    #     pass

    # @staticmethod
    # def issues_by_level(level: Level) -> Union[QuerySet, List['Issue']]:
    #     pass

    # @staticmethod
    # def issues_by_category(category: Category) -> Union[QuerySet, List['Issue']]:
    #     pass

    def save(self, *args, **kwargs):
        if not self.id:
            self.uuid = uuid_lib.uuid4()
        super(Sprint, self).save(*args, **kwargs)
