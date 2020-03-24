from .models import Collector
from .models import SpecimenRecord, SpecimenImage
from django import forms
import django_filters

class SpecimenRecordFilter(django_filters.FilterSet):
    usi = django_filters.CharFilter(lookup_expr='icontains', label='Specimen Identifier')
    order = django_filters.CharFilter(field_name='order__order_name', lookup_expr='icontains',
                                        label='Order')
    family = django_filters.CharFilter(field_name='family__family_name',
                                        lookup_expr='icontains', label='Family')
    subfamily = django_filters.CharFilter(field_name='subfamily__subfamily_name',
                                        lookup_expr='icontains', label='Subfamily')
    tribe = django_filters.CharFilter(field_name='tribe__tribe_name', lookup_expr='icontains',
                                        label='Tribe')
    genus = django_filters.CharFilter(field_name='genus__genus_name', lookup_expr='icontains',
                                        label='Genus')
    species = django_filters.CharFilter(field_name='species__species_name',
                                        lookup_expr='icontains', label='Species')
    subspecies = django_filters.CharFilter(field_name='subspecies__subspecies_name',
                                        lookup_expr='icontains', label='Subspecies')
    common_name = django_filters.CharFilter(field_name='common_name__common_name',
                                        lookup_expr='icontains', label='Common name')
    mona = django_filters.CharFilter(field_name='mona__mona', lookup_expr='icontains',
                                        label="MONA #")
    p3 = django_filters.CharFilter(field_name='p3__p3', lookup_expr='icontains', label='P3 #')
    determined_year = django_filters.CharFilter(lookup_expr='icontains', label='Determined year')
    preparation_date = django_filters.DateFilter(lookup_expr='icontains', label='Preparation date')
    county = django_filters.CharFilter(field_name='county__county_name', lookup_expr='icontains',
                                        label='County')
    locality = django_filters.CharFilter(field_name='locality__locality_name',
                                        lookup_expr='icontains', label='Locality')
    gps_latitude = django_filters.CharFilter(field_name='gps__latitude',
                                        lookup_expr='icontains', label='Latitude')
    gps_longitude = django_filters.CharFilter(field_name='gps__longitude',
                                        lookup_expr='icontains', label='Longitude')
    gps_elevation = django_filters.CharFilter(field_name='gps__elevation',
                                        lookup_expr='icontains', label='Elevation')
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
    usi_image = django_filters.CharFilter(field_name='usi_image__usi', lookup_expr='icontains', label='Specimen Identifier')
    species_page = django_filters.CharFilter(field_name='species_page__title', lookup_expr='icontains', label='Species')

    class Meta:
        model = SpecimenImage
        fields = ['usi_image', 'species_page', 'position']