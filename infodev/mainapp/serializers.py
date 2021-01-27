from rest_framework import serializers
from mainapp.models import WarningDevice


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class WarningDeviceSerializer(serializers.ModelSerializer):
    device_type = serializers.CharField(source='get_device_type_display')

    class Meta:
        model = WarningDevice
        fields = '__all__'
