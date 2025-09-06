from rest_framework import serializers
from .models import Result


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'created_at', 'type', 'target', 'result']
        read_only_fields = ['id', 'created_at']
