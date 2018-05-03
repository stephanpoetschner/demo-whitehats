from rest_framework import serializers

from consolelogs.models import ConsoleLog


class ConsoleLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsoleLog
        fields = ['stdout', ]
