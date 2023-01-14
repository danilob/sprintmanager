from rest_framework import serializers

from ..models import Level


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = [
            'id',
            'number_level',
            'days_min',
            'days_max',
            'devs_min',
            'devs_max',
        ]
