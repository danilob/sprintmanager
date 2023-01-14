from django.contrib import admin

from .models import Issue

from django.contrib.admin import SimpleListFilter


class WasLateIssueFilter(SimpleListFilter):
    title = 'was_late'
    parameter_name = 'was_late'
    IN_TIME = 'ON'
    OUT_TIME = 'OUT'
    NOT_FINISHED = 'FIN'

    def lookups(self, request, model_admin):
        return [
            (WasLateIssueFilter.IN_TIME, "concluded late"),
            (WasLateIssueFilter.OUT_TIME, "concluded on time"),
            (WasLateIssueFilter.NOT_FINISHED, "not finished"),
        ]

    def queryset(self, request, queryset):
        from django.db.models import F, Q
        from django.db.models.lookups import GreaterThan

        if not self.value():
            return queryset.all()
        if self.value() == WasLateIssueFilter.NOT_FINISHED:
            return queryset.filter(
                ~Q(status=Issue.DONE) & Q(finished_date__isnull=True)
            )
        else:
            return (
                queryset.filter(
                    Q(status=Issue.DONE) & Q(finished_date__isnull=False)
                )
                .annotate(
                    is_late=GreaterThan(
                        F('finished_date') - F('begin_date'),
                        F('forecast_date') - F('begin_date'),
                    )
                )
                .filter(is_late=(self.value() != WasLateIssueFilter.OUT_TIME))
            )


class IssueAdmin(admin.ModelAdmin):
    list_display = [
        'sprint',
        'description',
        'begin_date',
        'forecast_date',
        'finished_date',
        'status',
        'get_categories',  # 'categories',
        'was_late',
    ]
    search_fields = ['description']
    list_filter = [
        'status',
        #'was_late', is not possible
        WasLateIssueFilter,
    ]

    def get_categories(self, obj):
        # https://stackoverflow.com/questions/4424435/how-to-convert-a-django-queryset-to-a-list
        categories_query = obj.name_categories()
        return list(categories_query)


admin.site.register(Issue, IssueAdmin)
