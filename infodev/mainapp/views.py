from rest_framework import viewsets
from mainapp.models import WarningDevice
from mainapp.serializers import WarningDeviceSerializer
import django_filters.rest_framework
from rest_framework import filters
from django.views.generic import ListView


class MainView(ListView):
    model = WarningDevice
    context_object_name = 'devices'
    template_name = 'mainapp/main.html'
    paginate_by = 2


class WarningDeviceViewSet(viewsets.ModelViewSet):
    serializer_class = WarningDeviceSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'location_address']
    filterset_fields = ['device_type']

    def get_queryset(self):
        queryset = WarningDevice.objects.all()
        params = self.request.query_params
        if 'zone_radius_min' in params and params['zone_radius_min'] != '':
            queryset = queryset.filter(zone_radius__gte=params.get('zone_radius_min'))
        if 'zone_radius_max' in params and params['zone_radius_max'] != '':
            queryset = queryset.filter(zone_radius__lte=params.get('zone_radius_max'))
        if 'left_top' in params and 'right_bottom' in params\
                and params['left_top'] != '' and params['right_bottom'] != '':
            left_top_coords = params.get('left_top').split(',')
            right_bottom_coords = params.get('right_bottom').split(',')
            queryset = queryset.filter(
                latitude__lte=left_top_coords[0],
                longitude__gte=left_top_coords[1],
                latitude__gte=right_bottom_coords[0],
                longitude__lte=right_bottom_coords[1]
            )
        return queryset
