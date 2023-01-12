from django.contrib import admin

from .models import Sprint


class SprintAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sprint, SprintAdmin)
