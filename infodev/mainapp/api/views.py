from rest_framework import viewsets
from mainapp.models import WarningDevice
from mainapp.serializers import WarningDeviceSerializer
from rest_framework import filters
import django_filters


class WarningDeviceFilter(django_filters.FilterSet):
    zone_radius_min = django_filters.NumberFilter(field_name='zone_radius', lookup_expr='gte')
    zone_radius_max = django_filters.NumberFilter(field_name='zone_radius', lookup_expr='lte')

    class Meta:
        model = WarningDevice
        fields = ['zone_radius_min', 'zone_radius_max', 'device_type']


class WarningDeviceViewSet(viewsets.ModelViewSet):
    serializer_class = WarningDeviceSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'location_address']
    filterset_class = WarningDeviceFilter

    def get_queryset(self):
        queryset = WarningDevice.objects.all()
        params = self.request.query_params
        if 'right_bottom' in params and params.get('right_bottom') != '':
            right_bottom_coords = params.get('right_bottom').replace(' ', '').split(',')

            if len(right_bottom_coords) == 2:
                queryset = queryset.filter(
                    latitude__lte=right_bottom_coords[0],
                    longitude__lte=right_bottom_coords[1]
                )
            else:
                queryset = WarningDevice.objects.none()
        if 'left_top' in params and params.get('left_top') != '':
            left_top_coords = params.get('left_top').replace(' ', '').split(',')
            if len(left_top_coords) == 2:
                queryset = queryset.filter(
                    latitude__gte=left_top_coords[0],
                    longitude__gte=left_top_coords[1]
                )
            else:
                queryset = WarningDevice.objects.none()
        return queryset
