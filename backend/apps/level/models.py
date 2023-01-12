from django.db import models


class Level(models.Model):
    number_level = models.IntegerField(default=1)
    days_min = models.IntegerField(default=3)
    days_max = models.IntegerField(default=5)
    devs_min = models.IntegerField(default=1)
    devs_max = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Level'
        verbose_name_plural = 'Level'
        ordering = ['number_level']

    def __str__(self):
        return f'level - {self.number_level}'

    def save(self, *args, **kwargs):
        super(Level, self).save(*args, **kwargs)
