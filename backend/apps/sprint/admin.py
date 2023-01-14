from django.contrib import admin

from .models import Sprint


class SprintAdmin(admin.ModelAdmin):
    list_display = [
        'description',
        'issue_count',
        'has_finished',
        'was_late',
        'complexity_level',
    ]

    def get_queryset(self, request):
        # https://books.agiliq.com/projects/django-admin-cookbook/en/latest/sorting_calculated_fields.html
        from django.db.models import Sum

        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _level_complexity_sum=Sum("issue__level__number_level"),
        )
        return queryset

    def issue_count(self, obj):
        return obj.how_many_issues()

    def was_late(self, obj):
        return obj.is_sprint_delivered_late()

    def complexity_level(self, obj):
        return obj.complexity_level

    complexity_level.admin_order_field = '_level_complexity_sum'


admin.site.register(Sprint, SprintAdmin)
