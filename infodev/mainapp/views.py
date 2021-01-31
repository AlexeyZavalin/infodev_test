from mainapp.models import WarningDevice
from django.views.generic import ListView
from mainapp.forms import FilterForm, SearchForm


class MainView(ListView):
    model = WarningDevice
    context_object_name = 'devices'
    template_name = 'mainapp/main.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_form = FilterForm
        search_form = SearchForm
        context['filter_form'] = filter_form
        context['search_form'] = search_form
        return context
