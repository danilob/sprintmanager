from django.contrib import admin

from .models import Issue


class IssueAdmin(admin.ModelAdmin):
    list_display = [
        'sprint',
        'description',
        'begin_date',
        'forecast_date',
        'finished_date',
        'status',
    ]
    search_fields = ['description']
    list_filter = [
        'status',
    ]


admin.site.register(Issue, IssueAdmin)
