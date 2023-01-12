from django.contrib import admin

from .models import Level


class LevelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Level, LevelAdmin)
