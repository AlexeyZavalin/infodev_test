from rest_framework import viewsets
from mainapp.models import WarningDevice
from mainapp.serializers import WarningDeviceSerializer
import django_filters.rest_framework
from rest_framework import filters


class WarningDeviceViewSet(viewsets.ModelViewSet):
    serializer_class = WarningDeviceSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'location_address']
    filterset_fields = ['device_type']

    def get_queryset(self):
        queryset = WarningDevice.objects.all()
        params = self.request.query_params
        if 'zone_radius_min' in params and params.get('zone_radius_min') != '':
            queryset = queryset.filter(zone_radius__gte=params.get('zone_radius_min'))
        if 'zone_radius_max' in params and params['zone_radius_max'] != '':
            queryset = queryset.filter(zone_radius__lte=params.get('zone_radius_max'))
        if 'right_bottom' in params and params.get('right_bottom') != '':
            right_bottom_coords = params.get('right_bottom').split(',')
            queryset = queryset.filter(
                latitude__lte=right_bottom_coords[0],
                longitude__lte=right_bottom_coords[1]
            )
        if 'left_top' in params and params['left_top'] != '':
            left_top_coords = params.get('left_top').split(',')
            queryset = queryset.filter(
                latitude__gte=left_top_coords[0],
                longitude__gte=left_top_coords[1]
            )
        return queryset