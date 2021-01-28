from django.db import models

DEVICE_TYPE_CHOICES = [
    ('SR', 'Сирена'),
    ('SP', 'Громкоговоритель'),
]


class WarningDevice(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название')
    device_type = models.CharField(choices=DEVICE_TYPE_CHOICES, max_length=2, default=DEVICE_TYPE_CHOICES[0],
                                   verbose_name='Тип устройства')
    location_address = models.CharField(max_length=120, null=False, blank=True, verbose_name='Адрес размещения')
    latitude = models.DecimalField(decimal_places=6, max_digits=8, null=False, verbose_name='Широта')
    longitude = models.DecimalField(decimal_places=6, max_digits=9, null=False, verbose_name='Долгота')
    zone_radius = models.IntegerField(null=False, verbose_name='Радиус зоны звукопокрытия')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Устройства оповещения"
