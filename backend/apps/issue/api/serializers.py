from rest_framework import serializers

from ..models import Issue
from apps.sprint.models import Sprint
from apps.category.models import Category


class SprintRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value.uuid)

    def to_internal_value(self, data):
        return Sprint.objects.get(uuid=data)


class CategoryRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value.uuid)

    def to_internal_value(self, data):
        return Category.objects.get(uuid=data)


class IssueRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value.uuid)

    def to_internal_value(self, data):
        return Issue.objects.get(uuid=data)


class IssueSerializer(serializers.ModelSerializer):
    sprint = SprintRelatedField(queryset=Sprint.objects.all(), many=False)
    categories = CategoryRelatedField(queryset=Category.objects.all(), many=True)
    dependencies = IssueRelatedField(queryset=Issue.objects.all(), many=True)

    class Meta:
        model = Issue
        fields = [
            'uuid',
            'sprint',
            'categories',
            'level',
            'dependencies',
            'begin_date',
            'description',
            'forecast_date',
            'finished_date',
            'url',
            'status',
        ]
        extra_kwargs = {'sprint': {'required': False}}

    # def validate_description(self, value):
    #     from django.forms import ValidationError

    #     if len(value) <= 4:
    #         raise ValidationError("Deve ter pelo menos cinco caracteres.")
    #     return value
