from django.contrib import admin
from mainapp.models import WarningDevice


@admin.register(WarningDevice)
class WarningDeviceAdmin(admin.ModelAdmin):
    pass
