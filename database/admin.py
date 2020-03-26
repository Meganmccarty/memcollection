from django.contrib import admin
from database.models import Determiner, Preparer, Collector
from database.models import CommonName, TaxonAuthority, Mona, P3
from database.models import Order, Family, Subfamily, Tribe, Genus, Species, Subspecies
from database.models import SpeciesImage, ImmatureImage, MapImage, HostPlantImage, AdultFoodImage, HabitatImage, PredatorImage
from database.models import SpeciesPage
from database.models import Country, State, County, Locality, Gps, CollectingTrip, CollectingTripImage
from database.models import SpecimenImage, SpecimenRecord

# AGENT Models #

admin.site.register(Determiner)
admin.site.register(Preparer)
admin.site.register(Collector)


# BASIC Models #

admin.site.register(CommonName)
admin.site.register(TaxonAuthority)
admin.site.register(Mona)
admin.site.register(P3)


# TAXON Models #

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_name', 'order_authority', 'order_common_name')

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('order', 'family_name', 'family_authority', 'family_common_name')

@admin.register(Subfamily)
class SubfamilyAdmin(admin.ModelAdmin):
    list_display = ('family', 'subfamily_name', 'subfamily_authority', 'subfamily_common_name')

@admin.register(Tribe)
class TribeAdmin(admin.ModelAdmin):
    list_display = ('subfamily', 'tribe_name', 'tribe_authority', 'tribe_common_name')

@admin.register(Genus)
class GenusAdmin(admin.ModelAdmin):
    list_display = ('tribe', 'genus_name', 'genus_authority', 'genus_common_name')

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('genus', 'species_name', 'species_authority', 'species_common_name', 'species_mona', 'species_p3')
    fields = ['genus', 'species_name', 'species_authority', 'species_common_name', ('species_mona', 'species_p3')]

@admin.register(Subspecies)
class SubspeciesAdmin(admin.ModelAdmin):
    list_display = ('species', 'subspecies_name', 'subspecies_authority', 'subspecies_common_name', 'subspecies_mona', 'subspecies_p3')
    fields = ['species', 'subspecies_name', 'subspecies_authority', 'subspecies_common_name', ('subspecies_mona', 'subspecies_p3')]


# SPECIES PAGE Models #

@admin.register(SpeciesImage)
class SpeciesImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'species', 'caption', 'species_page')

class SpeciesImageInline(admin.TabularInline):
    model = SpeciesImage
    extra = 0

@admin.register(ImmatureImage)
class ImmatureImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'species', 'caption', 'species_page')

class ImmatureImageInline(admin.TabularInline):
    model = ImmatureImage
    extra = 0

@admin.register(MapImage)
class MapImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'species', 'caption', 'species_page')

class MapImageInline(admin.TabularInline):
    model = MapImage
    extra = 0

@admin.register(HostPlantImage)
class HostPlantImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'species', 'caption', 'species_page')

class HostPlantImageInline(admin.TabularInline):
    model = HostPlantImage
    extra = 0

@admin.register(AdultFoodImage)
class AdultFoodImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'species', 'caption', 'species_page')

class AdultFoodImageInline(admin.TabularInline):
    model = AdultFoodImage
    extra = 0

@admin.register(HabitatImage)
class HabitatImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'species', 'caption', 'species_page')

class HabitatImageInline(admin.TabularInline):
    model = HabitatImage
    extra = 0

@admin.register(PredatorImage)
class PredatorImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'species', 'caption', 'species_page')

class PredatorImageInline(admin.TabularInline):
    model = PredatorImage
    extra = 0

@admin.register(SpeciesPage)
class SpeciesPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'species_name', 'taxonomy', 'description', 'similar_species', 'distribution', 'habitat', 'seasonality', 'host_plants', 'adult_food', 'behavior', 'ecology', 'life_cycle', 'references')
    inlines = [SpeciesImageInline, ImmatureImageInline, MapImageInline, HostPlantImageInline, AdultFoodImageInline, HabitatImageInline, PredatorImageInline]
    fields = ['title', 'species_name', 'taxonomy', 'description', 'similar_species', 'distribution', 'habitat', 'seasonality', 'host_plants', 'adult_food', 'behavior', 'ecology', 'life_cycle', 'references']


# LOCALITY Models #

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fields = [('country_name', 'country_abbr')]

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('country', 'state_name', 'state_abbr')
    fields = ['country', ('state_name', 'state_abbr')]

@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ('state', 'county_name')

@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    list_display = ('country', 'state', 'county', 'get_range', 'get_town', 'get_locality')
    fields = ['locality_name', ('country', 'state', 'county'), ('range', 'town')]

@admin.register(Gps)
class GpsAdmin(admin.ModelAdmin):
    list_display = ('locality', 'get_latitude', 'get_longitude', 'get_elevation')
    fields = ['locality', ('latitude', 'longitude', 'elevation')]

@admin.register(CollectingTripImage)
class CollectingTripImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'caption', 'collecting_trip')
    fields = ['image', 'caption', 'collecting_trip']

class CollectingTripImageInline(admin.TabularInline):
    model = CollectingTripImage
    extra = 0

@admin.register(CollectingTrip)
class CollectingTripAdmin(admin.ModelAdmin):
    list_display = ('trip_name', 'display_states', 'start_date', 'end_date')
    inlines = [CollectingTripImageInline]
    fields = ['trip_name', 'states_collected', ('start_date', 'end_date'), 'notes']


# SPECIMEN Models #

@admin.register(SpecimenImage)
class SpecimenImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'position')

class SpecimenImageInline(admin.TabularInline):
    model = SpecimenImage
    extra = 0

@admin.register(SpecimenRecord)
class SpecimenRecordAdmin(admin.ModelAdmin):
    list_display = ('usi', 'order', 'family', 'subfamily', 'tribe', 'genus', 'species', 'subspecies', 'authority', 'common_name', 'mona', 'p3', 'species_page', 'determiner', 'determined_year', 'sex', 'stage', 'preparer', 'preparation', 'preparation_date', 'printed', 'labeled', 'photographed', 'collecting_trip', 'country', 'state', 'county', 'locality', 'gps', 'get_date', 'display_collector', 'method', 'weather', 'get_temperatureC', 'get_temperatureF', 'time_of_day', 'habitat_notes', 'other_notes')
    inlines = [SpecimenImageInline]
    fieldsets = (
        ('Specimen Details', {
            'fields': ['usi', ('order', 'family', 'subfamily', 'tribe', 'genus', 'species', 'subspecies'), ('authority', 'common_name', 'mona', 'p3'), 'species_page', ('determiner', 'determined_year'), ('sex', 'stage'), ('preparer', 'preparation', 'preparation_date'), 'printed', 'labeled', 'photographed']
        }),
        ('Locality Details', {
            'fields': ['collecting_trip', ('country', 'state', 'county'), 'locality', 'gps', ('day', 'month', 'year'), 'collector', 'method', ('weather', 'temperatureC', 'temperatureF', 'time_of_day'), 'habitat_notes', 'other_notes']
        }),
    )