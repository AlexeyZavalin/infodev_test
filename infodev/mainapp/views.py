from rest_framework import viewsets
from mainapp.models import WarningDevice
from mainapp.serializers import WarningDeviceSerializer
import django_filters.rest_framework
from rest_framework import filters
from django.views.generic import ListView
from mainapp.forms import FilterForm


class MainView(ListView):
    model = WarningDevice
    context_object_name = 'devices'
    template_name = 'mainapp/main.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = FilterForm
        context['filter_form'] = form
        return context
