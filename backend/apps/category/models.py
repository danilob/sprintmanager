from django.db import models

import uuid as uuid_lib


class Category(models.Model):
    description = models.CharField(max_length=100)
    uuid = models.UUIDField(
        db_index=True, default=uuid_lib.uuid4, unique=True, editable=False
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['description']

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        if not self.id:
            self.uuid = uuid_lib.uuid4()
        super(Category, self).save(*args, **kwargs)
