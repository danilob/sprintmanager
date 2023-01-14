from rest_framework import serializers

from ..models import Sprint


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = [
            'uuid',
            'description',
            'begin_date',
            'forecast_date',
            'finished_date',
            'url',
        ]
