from rest_framework import serializers
from mainapp.models import WarningDevice


class WarningDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarningDevice
        fields = '__all__'
