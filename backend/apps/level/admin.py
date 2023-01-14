from django.contrib import admin

from .models import Level


class LevelAdmin(admin.ModelAdmin):
    list_display = [
        'number_level',
        'days',
        'devs',
    ]


admin.site.register(Level, LevelAdmin)
