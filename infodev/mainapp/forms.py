from django import forms
from mainapp.models import DEVICE_TYPE_CHOICES


class FilterForm(forms.Form):
    device_type = forms.ChoiceField(label='Тип устройства', choices=DEVICE_TYPE_CHOICES)
    left_top = forms.CharField(label='Координаты верхнего левого угла', max_length=50, required=False)
    right_bottom = forms.CharField(label='Координаты правого нижнего угла', max_length=50, required=False)
    zone_radius_min = forms.IntegerField(label='Минимальный радиус зоны звукопокрытия', required=False)
    zone_radius_max = forms.IntegerField(label='Максимальный радиус зоны звукопокрытия', required=False)


class SearchForm(forms.Form):
    search = forms.CharField(label='Поиск')
