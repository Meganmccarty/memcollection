from .models import Collector
from .models import SpecimenRecord, SpecimenImage
from django import forms
import django_filters

class SpecimenRecordFilter(django_filters.FilterSet):
    usi = django_filters.CharFilter(lookup_expr='icontains', label='Specimen Identifier')
    determined_year = django_filters.CharFilter(lookup_expr='icontains', label='Determined year')
    preparation_date = django_filters.DateFilter(lookup_expr='icontains', label='Preparation date')
    day = django_filters.CharFilter(lookup_expr='icontains', label='Day')
    month = django_filters.CharFilter(lookup_expr='icontains', label='Month')
    year = django_filters.CharFilter(lookup_expr='icontains', label='Year')
    collector = django_filters.ModelMultipleChoiceFilter(queryset=Collector.objects.all(), widget=forms.CheckboxSelectMultiple)
    weather = django_filters.CharFilter(lookup_expr='icontains', label='Weather')
    temperatureC = django_filters.CharFilter(lookup_expr='icontains', label='Temperature (°C)')
    temperatureF = django_filters.CharFilter(lookup_expr='icontains', label='Temperature (°F)')
    time_of_day = django_filters.CharFilter(lookup_expr='icontains', label='Time of day')
    habitat_notes = django_filters.CharFilter(lookup_expr='icontains', label='Habitat notes')
    other_notes = django_filters.CharFilter(lookup_expr='icontains', label='Other notes')

    class Meta:
        model = SpecimenRecord
        fields = ['usi', 'order', 'family', 'subfamily', 'tribe', 'genus', 'species', 'subspecies', 'common_name', 'mona', 'p3', \
            'sex', 'stage', 'determiner', 'determined_year', 'preparer', 'preparation', 'preparation_date', 'collecting_trip', \
            'country', 'state', 'county', 'locality', 'gps', 'day', 'month', 'year', 'collector', 'method', 'weather', \
            'temperatureC', 'temperatureF', 'time_of_day', 'habitat_notes', 'other_notes']

class SpecimenImageFilter(django_filters.FilterSet):
    usi_image = django_filters.CharFilter(label='Specimen Identifier')
    species_page = django_filters.CharFilter(label='Species')

    class Meta:
        model = SpecimenImage
        fields = ['usi_image', 'species_page', 'position']