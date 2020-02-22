from django.db import models
from django.urls import reverse
from sorl.thumbnail import ImageField

### AGENT MODELS (DETERMINER, PREPARER, COLLECTOR) ###

class Determiner(models.Model):
    name = models.CharField(max_length=100, help_text='Enter the full name of the determiner, ' \
    'including middle initial.')
    class Meta:
        ordering = ['name']
    def __str__(self):
        return f'{self.name}'

class Preparer(models.Model):
    name = models.CharField(max_length=100, help_text='Enter the full name of the determiner, ' \
    'including middle initial.')
    class Meta:
        ordering = ['name']
    def __str__(self):
        return f'{self.name}'

class Collector(models.Model):
    name = models.CharField(max_length=100, help_text='Enter the full name of the determiner, ' \
    'including middle initial.')
    class Meta:
        ordering = ['name']
    def __str__(self):
        return f'{self.name}'

### BASIC MODELS (COMMON NAME, TAXON AUTHORITY, MONA, P3) ###

class CommonName(models.Model):
    common_name = models.CharField(max_length=200, help_text='Enter a common name for a taxon.')
    class Meta:
        ordering = ['common_name']
    def __str__(self):
        return f'{self.common_name}'

class TaxonAuthority(models.Model):
    authority = models.CharField(max_length=100, help_text='Enter an author and year of ' \
    'publication for a taxon description.')
    class Meta:
        ordering = ['authority']
        verbose_name_plural = 'Taxon authorities'
    def __str__(self):
        return f'{self.authority}'

class Mona(models.Model):
    mona = models.DecimalField(max_digits=8, decimal_places=2, \
        help_text='Enter the MONA (Hodges) # for a species (Lepidoptera only).')
    class Meta:
        ordering = ['mona']
        verbose_name_plural = 'Mona numbers'
    def __str__(self):
        return f'{self.mona}'

class P3(models.Model):
    p3 = models.DecimalField(max_digits=8, decimal_places=1, \
        help_text='Enter the P3 (Pohl, Patterson, Pelham 2016) # for a species (Lepidoptera only).')
    class Meta:
        ordering = ['p3']
        verbose_name_plural = 'P3 numbers'
    def __str__(self):
        return f'{self.p3}'

### TAXON MODELS (ORDER, FAMILY, SUBFAMILY, TRIBE, GENUS, SPECIES, SUBSPECIES) ###

class Order(models.Model):
    order_name = models.CharField(max_length=200, help_text='Enter the name of the order.')
    order_authority = models.ForeignKey(TaxonAuthority, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the authority for the order.')
    order_common_name = models.ForeignKey(CommonName, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the common name of the order, if it has one.')
    class Meta:
        ordering = ['order_name']
    def __str__(self):
        return f'{self.order_name}'

class Family(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, \
        help_text='Select the order to which this family belongs.')
    family_name = models.CharField(max_length=200, help_text='Enter the name of the family.')
    family_authority = models.ForeignKey(TaxonAuthority, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the authority for the family.')
    family_common_name = models.ForeignKey(CommonName, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the common name of the family, if it has one.')
    class Meta:
        ordering = ['family_name']
        verbose_name_plural = 'Families'
    def __str__(self):
        return f'{self.family_name}'

class Subfamily(models.Model):
    family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True, \
        help_text='Select the family to which this subfamily belongs.')
    subfamily_name = models.CharField(max_length=200, help_text='Enter the name of the subfamily.')
    subfamily_authority = models.ForeignKey(TaxonAuthority, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the authority for the subfamily.')
    subfamily_common_name = models.ForeignKey(CommonName, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the common name of the subfamily, if it has one.')
    class Meta:
        ordering = ['subfamily_name']
        verbose_name_plural = 'Subfamilies'
    def __str__(self):
        return f'{self.subfamily_name}'

class Tribe(models.Model):
    subfamily = models.ForeignKey(Subfamily, on_delete=models.SET_NULL, null=True, \
        help_text='Select the subfamily to which this tribe belongs.')
    tribe_name = models.CharField(max_length=200, help_text='Enter the name of the tribe.')
    tribe_authority = models.ForeignKey(TaxonAuthority, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the authority for the tribe.')
    tribe_common_name = models.ForeignKey(CommonName, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the common name of the tribe, if it has one.')
    class Meta:
        ordering = ['tribe_name']
    def __str__(self):
        return f'{self.tribe_name}'

class Genus(models.Model):
    tribe = models.ForeignKey(Tribe, on_delete=models.SET_NULL, null=True, \
        help_text='Select the tribe to which this genus belongs.')
    genus_name = models.CharField(max_length=200, help_text='Enter the name of the genus.')
    genus_authority = models.ForeignKey(TaxonAuthority, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the authority for the genus.')
    genus_common_name = models.ForeignKey(CommonName, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the common name of the genus, if it has one.')
    class Meta:
        ordering = ['genus_name']
        verbose_name_plural = 'Genera'
    def __str__(self):
        return f'{self.genus_name}'

class Species(models.Model):
    genus = models.ForeignKey(Genus, on_delete=models.SET_NULL, null=True, \
        help_text='Select the genus to which this species belongs.')
    species_name = models.CharField(max_length=200, help_text='Enter the name of the species.')
    species_authority = models.ForeignKey(TaxonAuthority, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the authority for the species.')
    species_common_name = models.ForeignKey(CommonName, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the common name of the species, if it has one.')
    species_mona = models.ForeignKey(Mona, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the MONA (Hodges) # for the species (Lepidoptera only).')
    species_p3 = models.ForeignKey(P3, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the P3 (Pohl, Patterson, Pelham 2016) # for the species (Lepidoptera only).')
    class Meta:
        ordering = ['species_name']
        verbose_name_plural = 'Species'
    def __str__(self):
        return f'{self.species_name}'

class Subspecies(models.Model):
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, \
        help_text='Select the species to which this subspecies belongs.')
    subspecies_name = models.CharField(max_length=200, null=True, blank=True, \
        help_text='Enter the name of the subspecies.')
    subspecies_authority = models.ForeignKey(TaxonAuthority, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the authority for the subspecies.')
    subspecies_common_name = models.ForeignKey(CommonName, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the common name of the subspecies, if it has one.')
    subspecies_mona = models.ForeignKey(Mona, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the MONA (Hodges) # for the subspecies (Lepidoptera only). ' \
        'If it lacks its own # but the nominate species has one, enter the nominate species # here.')
    subspecies_p3 = models.ForeignKey(P3, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the P3 (Pohl, Patterson, Pelham 2016) # for the subspecies (Lepidoptera only). ' \
        'If it lacks its own # but the nominate species has one, enter the nominate species # here.')
    class Meta:
        ordering = ['subspecies_name']
        verbose_name_plural = 'Subspecies'
    def __str__(self):
        return f'{self.subspecies_name}'

### IMAGE MODELS (ADULT, IMMATURE, MAP, HOST PLANT, ADULT FOOD, HABITAT, PREDATOR, SPECIMEN) ###

class SpeciesImage(models.Model):
    image = ImageField(upload_to='images/speciespage/adults')
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, help_text='Select the species.')
    caption = models.CharField(max_length=500, null=True, blank=True, help_text='Enter a caption for the image.')
    species_page = models.ForeignKey('SpeciesPage', on_delete=models.SET_NULL, null=True, \
        help_text='Select the species page.')
    class Meta:
        ordering = ['image']
    def __str__(self):
        return f'{self.image}'

class ImmatureImage(models.Model):
    image = ImageField(upload_to='images/speciespage/immatures')
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, help_text='Select the species.')
    caption = models.CharField(max_length=500, null=True, blank=True, help_text='Enter a caption for the image.')
    species_page = models.ForeignKey('SpeciesPage', on_delete=models.SET_NULL, null=True, \
        help_text='Select the species page.')
    class Meta:
        ordering = ['image']
    def __str__(self):
        return f'{self.image}'

class MapImage(models.Model):
    image = ImageField(upload_to='images/speciespage/maps')
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, help_text='Select the species.')
    caption = models.CharField(max_length=500, null=True, blank=True, help_text='Enter a caption for the image.')
    species_page = models.ForeignKey('SpeciesPage', on_delete=models.SET_NULL, null=True, \
        help_text='Select the species page.')
    class Meta:
        ordering = ['image']
    def __str__(self):
        return f'{self.image}'

class HostPlantImage(models.Model):
    image = ImageField(upload_to='images/speciespage/hostplants')
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, help_text='Select the species.')
    caption = models.CharField(max_length=500, null=True, blank=True, help_text='Enter a caption for the image.')
    species_page = models.ForeignKey('SpeciesPage', on_delete=models.SET_NULL, null=True, \
        help_text='Select the species page.')
    class Meta:
        ordering = ['image']
    def __str__(self):
        return f'{self.image}'

class AdultFoodImage(models.Model):
    image = ImageField(upload_to='images/speciespage/adultfood')
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, help_text='Select the species.')
    caption = models.CharField(max_length=500, null=True, blank=True, help_text='Enter a caption for the image.')
    species_page = models.ForeignKey('SpeciesPage', on_delete=models.SET_NULL, null=True, \
        help_text='Select the species page.')
    class Meta:
        ordering = ['image']
    def __str__(self):
        return f'{self.image}'

class HabitatImage(models.Model):
    image = ImageField(upload_to='images/speciespage/habitats')
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, help_text='Select the species.')
    caption = models.CharField(max_length=500, null=True, blank=True, help_text='Enter a caption for the image.')
    species_page = models.ForeignKey('SpeciesPage', on_delete=models.SET_NULL, null=True, \
        help_text='Select the species page.')
    class Meta:
        ordering = ['image']
    def __str__(self):
        return f'{self.image}'

class PredatorImage(models.Model):
    image = ImageField(upload_to='images/speciespage/predators')
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, help_text='Select the species.')
    caption = models.CharField(max_length=500, null=True, blank=True, help_text='Enter a caption for the image.')
    species_page = models.ForeignKey('SpeciesPage', on_delete=models.SET_NULL, null=True, \
        help_text='Select the species page.')
    class Meta:
        ordering = ['image']
    def __str__(self):
        return f'{self.image}'

class SpecimenImage(models.Model):
    POSITION = (
        ('dorsal', 'Dorsal'),
        ('ventral', 'Ventral'),
        ('lateral', 'Lateral'),
    )
    image = ImageField(upload_to='images/specimens')
    position = models.CharField(max_length=20, choices=POSITION, null=True, blank=True, \
        verbose_name='Specimen View', help_text='Select the view of the specimen.')
    usi_image = models.ForeignKey('SpecimenRecord', on_delete=models.SET_NULL, null=True, blank=True, \
        verbose_name='Unique Specimen Identifier', help_text='Enter the unique specimen identifier for the ' \
        'specimen in the image.')
    species_page = models.ForeignKey('SpeciesPage', on_delete=models.SET_NULL, null=True, blank=True, \
        verbose_name='Species Page', help_text='Select the species page for this image, if it has one.')
    class Meta:
        ordering = ['image', 'usi_image']
    def __str__(self):
        return f'{self.image}'

### LOCALITY MODELS (COUNTRY, STATE, COUNTY, LOCALITY, GPS) ###

class Country(models.Model):
    country_name = models.CharField(max_length=100, help_text='Enter the name of the country.')
    country_abbr = models.CharField(max_length=5, verbose_name='Abbreviation', \
        help_text='Enter the abbreviation for the country.')
    class Meta:
        ordering = ['country_name']
        verbose_name_plural = 'Countries'
    def __str__(self):
        return f'{self.country_abbr}'

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, \
        help_text='Select the country to which this state belongs.')
    state_name = models.CharField(max_length=100, help_text='Enter the name of the state.')
    state_abbr = models.CharField(max_length=5, verbose_name='Abbreviation', \
        help_text='Enter the abbreviation for the state.')
    class Meta:
        ordering = ['state_name']
    def __str__(self):
        return f'{self.state_abbr}'

class County(models.Model):
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, \
        help_text='Select the state to which this county belongs.')
    county_name = models.CharField(max_length=100, help_text='Enter the name of the county.')
    class Meta:
        ordering = ['county_name']
        verbose_name_plural = 'Counties'
    def __str__(self):
        return f'{self.county_name}'

class Locality(models.Model):
    locality_name = models.CharField(max_length=200, null=True, blank=True, help_text='Enter a name for the locality.')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the country to which this locality belongs.')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the state to which this locality belongs.')
    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the county to which this locality belongs.')
    range = models.CharField(max_length=50, null=True, blank=True, help_text='Enter the range from ' \
        'the nearest town to which this locality belongs.')
    town = models.CharField(max_length=200, null=True, blank=True, \
        help_text='Enter the nearest town to this locality.')
    class Meta:
        ordering = ['range', 'town', 'locality_name']
        verbose_name_plural = 'Localities'
    @property
    def get_locality(self):
        if self.locality_name:
            return self.locality_name
        else:
            return ""
    @property
    def get_range(self):
        if self.range:
            return self.range
        else:
            return ""
    @property
    def get_town(self):
        if self.town:
            return self.town
        else:
            return ""
    def __str__(self):
        return f'{self.get_range} {self.get_town}: {self.get_locality}'

class Gps(models.Model):
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the locality to which these GPS data belong.')
    latitude = models.DecimalField(max_digits=12, decimal_places=8, null=True, blank=True, \
        help_text='Enter the latitude, in decimal degrees.')
    longitude = models.DecimalField(max_digits=12, decimal_places=8, null=True, blank=True, \
        help_text='Enter the longitute, in decimal degrees (use "-" instead of "W").')
    elevation = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, \
        verbose_name = 'Elevation (meters)', help_text='Enter the elevation, in meters.')
    class Meta:
        ordering = ['latitude', 'longitude']
        verbose_name_plural = 'GPS'
    @property
    def get_latitude(self):
        if self.latitude:
            return self.latitude
        else:
            return ""
    @property
    def get_longitude(self):
        if self.longitude:
            return self.longitude
        else:
            return ""
    @property
    def get_elevation(self):
        if self.elevation:
            return f'{self.elevation}m'
        else:
            return ""
    def __str__(self):
        return f'{self.get_latitude} {self.get_longitude} {self.get_elevation}'

### COLLECTING TRIP MODELS (COLLECTING TRIP, COLLECTING TRIP IMAGE) ###

class CollectingTrip(models.Model):
    trip_name = models.CharField(primary_key=True, max_length=200, \
        help_text='Enter a name for the collecting trip.')
    start_date = models.DateField(help_text='Enter the start date of the trip.')
    end_date = models.DateField(help_text='Enter the end date of the trip.')
    notes = models.TextField(null=True, blank=True, max_length=20000, \
        help_text='Enter any details about the trip (such as journal notes).')
    class Meta:
        ordering = ['trip_name']
    def __str__(self):
        return f'{self.trip_name}'
    def get_absolute_url(self):
        return reverse('collecting-trip-detail', args=[str(self.pk)])

class CollectingTripImage(models.Model):
    image = ImageField(upload_to='images/collecting-trips')
    caption = models.CharField(max_length=500, null=True, blank=True, \
        help_text='Enter a caption for the image.')
    collecting_trip = models.ForeignKey(CollectingTrip, on_delete=models.SET_NULL, null=True, \
        help_text='Select the collecting trip to which this image belongs.')
    class Meta:
        ordering = ['image']
    def __str__(self):
        return f'{self.image}'

### SPECIES PAGE AND SPECIMEN RECORD MODELS ###

class SpeciesPage(models.Model):
    title = models.CharField(max_length=100, primary_key=True, help_text='Enter a title for the page.')
    species_name = models.OneToOneField(Species, on_delete=models.SET_NULL, null=True, \
        help_text='Select the species for this page.')
    taxonomy = models.TextField(max_length=100000, null=True, blank=True, \
        help_text='Include any info about the taxonomy of the species, such as synonyms, subspecies, forms, etc.')
    description = models.TextField(max_length=100000, null=True, blank=True, \
        help_text='Write a description for the species.')
    similar_species = models.TextField(max_length=100000, null=True, blank=True, \
        help_text='Write a section about species similar to the one described on the page.')
    distribution = models.TextField(max_length=100000, null=True, blank=True, \
        help_text='Write a section about where the species is found.')
    habitat = models.TextField(max_length=100000, null=True, blank=True, \
        help_text='Write a section about what kind of habitat the species is found in.')
    seasonality = models.TextField(max_length=100000, null=True, blank=True, \
        help_text='Write a section about the flight period of the species/number of broods.')
    host_plants = models.TextField(max_length=100000, null=True, blank=True, \
        help_text='Write a section about the larval food plants, and what parts of the plant the species eats.')
    adult_food = models.TextField(max_length=100000, null=True, blank=True, \
        help_text='Write a section about what the adult feeds on (such as nectar sources).')
    behavior = models.TextField(max_length=100000, null=True, blank=True, \
        help_text='Write a section about the behavior of the species.')
    ecology = models.TextField(max_length=100000, null=True, blank=True, \
        help_text='Write a section about the ecology of the species.')
    life_cycle = models.TextField(max_length=100000, null=True, blank=True, \
        help_text='Write a section about the complete life cycle of the species.')
    references = models.TextField(max_length=1000000, null=True, blank=True, \
        help_text='Enter the reference(s) used in the article.')
    class Meta:
        ordering = ['title']
    def __str__(self):
        return f'{self.title}'
    def get_absolute_url(self):
        return reverse('species-page', args=[str(self.pk)])

class SpecimenRecord(models.Model):
    usi = models.CharField(primary_key=True, max_length=20, verbose_name='Specimen Identifier', \
        help_text='Enter the unique identifier for the specimen.')
#Taxon Info
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the order for this specimen, if known.')
    family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the family for this specimen, if known.')
    subfamily = models.ForeignKey(Subfamily, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the subfamily for this specimen, if known.')
    tribe = models.ForeignKey(Tribe, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the tribe for this specimen, if known.')
    genus = models.ForeignKey(Genus, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the genus for this specimen, if known.')
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the species for this specimen, if known.')
    subspecies = models.ForeignKey(Subspecies, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the subspecies for this specimen, if known.')
    authority = models.ForeignKey(TaxonAuthority, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the authority for this specimen.')
    common_name = models.ForeignKey(CommonName, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the common name for this specimen, if it has one.')
    mona = models.ForeignKey(Mona, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the MONA (Hodges) # for this specimen (Lepidoptera only).')
    p3 = models.ForeignKey(P3, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the P3 (Pohl, Patterson, and Pelham 2016) # for this specimen (Lepidoptera only).')
    species_page = models.ForeignKey(SpeciesPage, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the species page for this specimen, if it has one/if it has been identified to species/subspecies.')
    determiner = models.ForeignKey(Determiner, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the person who made the determination, if any above.')
    determined_year = models.IntegerField(null=True, blank=True, \
        help_text='Enter the year the determination was made, if any.')
#Specimen Info
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unknown', 'Unknown'),
    )
    STAGE = (
        ('Egg', 'Egg'),
        ('Larva', 'Larva'),
        ('Nymph', 'Nymph'),
        ('Pupa', 'Pupa'),
        ('Adult', 'Adult'),
    )
    PREPARATION_TYPE = (
        ('Spread', 'Spread'),
        ('Pinned', 'Pinned'),
        ('Minuten', 'Minuten'),
        ('Pointed', 'Pointed'),
        ('Envelope.', 'Envelope'),
        ('Container', 'Container'),
        ('Alcohol', 'Alcohol'),
    )
    sex = models.CharField(max_length=20, choices=SEX, blank=True, default='', \
        help_text='Select the sex of the specimen, if known.')
    stage = models.CharField(max_length=20, choices=STAGE, blank=True, default='', \
        help_text='Select the stage of the specimen.')
    preparer = models.ForeignKey(Preparer, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Enter the person who prepared the specimen.')
    preparation = models.CharField(max_length=20, choices=PREPARATION_TYPE, blank=True, default='', \
        help_text='Select the method with which the specimen was prepared.')
    preparation_date = models.DateField(null=True, blank=True, help_text='Enter the date the specimen was pinned/spread.')
    printed = models.BooleanField(verbose_name='Are the labels for the specimen printed?')
    labeled = models.BooleanField(verbose_name='Is the specimen labeled?')
    photographed = models.BooleanField(verbose_name='Is the specimen photographed?')
#Locality Info
    collecting_trip = models.ForeignKey(CollectingTrip, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Enter the name of the collecting trip on which the specimen was collected, if any.')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the country from which this specimen was collected.')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the state from which this specimen was collected.')
    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the county from which this specimen was collected.')
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the locality from which this specimen was collected.')
    gps = models.ForeignKey(Gps, on_delete=models.SET_NULL, null=True, blank=True, \
        help_text='Select the GPS data from which this specimen was collected.')
    day = models.IntegerField(null=True, blank=True, help_text='Enter the day the specimen was collected, if known.')
    MONTH = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )
    month = models.CharField(max_length=20, choices=MONTH, blank=True, default='', \
        help_text='Select the month the specimen was collected, if known.')
    year = models.IntegerField(null=True, blank=True, help_text='Enter the year the specimen was collected, if known.')
    collector = models.ManyToManyField(Collector, verbose_name='Collector(s)', blank=True, \
        help_text='Enter the name of the specimen collector(s).')
#Method/Other Info
    METHOD = (
        ('Net', 'Net'),
        ('Reared', 'Reared'),
        ('Trap', 'Trap'),
        ('UV trap', 'UV Trap'),
        ('Light', 'Light'),
        ('MV light', 'MV Light'),
        ('MV light sheet', 'MV Light Sheet'),
        ('UV light', 'UV Light'),
        ('UV light sheet', 'UV Light Sheet'),
        ('UV/MV light sheet', 'UV/MV Light Sheet'),
        ('Bait', 'Bait'),
        ('By hand', 'By Hand'),
        ('Sweep', 'Sweep'),
    )
    method = models.CharField(max_length=30, choices=METHOD, blank=True, default='', \
        help_text='Select the method used to capture the specimen.')
    weather = models.CharField(max_length=100, null=True, blank=True, \
        help_text='Enter the weather conditions that occurred during the time the specimen was collected.')
    temperatureC = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, \
        verbose_name='Temperature (°C)', help_text='Enter the temperature (Celsius) ' \
        'outside at which the specimen was collected.')
    temperatureF = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, \
        verbose_name='Temperature (°F)', help_text='Enter the temperature (Fahrenheit) outside ' \
        'at which the specimen was collected.')
    time_of_day = models.CharField(max_length=50, null=True, blank=True, \
        help_text='Enter details about time of day the specimen was collected.')
    habitat_notes = models.TextField(max_length=1000, null=True, blank=True, \
        help_text='Enter details about the habitat in which the specimen was collected.')
    other_notes = models.TextField(max_length=2000, null=True, blank=True, \
        help_text='Enter any other details regarding the specimen.')
    class Meta:
        ordering = ['usi', 'p3', 'order']
#Taxon Functions
    @property
    def get_order(self):
        if self.order:
            return self.order
        else:
            return ""
    @property
    def get_family(self):
        if self.family:
            return self.family
        else:
            return ""
    @property
    def get_subfamily(self):
        if self.subfamily:
            return self.subfamily
        else:
            return ""
    @property
    def get_tribe(self):
        if self.tribe:
            return self.tribe
        else:
            return ""
    @property
    def get_genus(self):
        if self.genus:
              return self.genus
        else:
              return ""
    @property
    def get_species(self):
        if self.species:
              return self.species
        else:
              return ""
    @property
    def get_subspecies(self):
        if self.subspecies:
            return self.subspecies
        else:
            return ""
    @property
    def get_authority(self):
        if self.authority:
            return self.authority
        else:
            return ""
    @property
    def get_common_name(self):
        if self.common_name:
              return self.common_name
        else:
              return ""
    @property
    def get_mona(self):
        if self.mona:
            return self.mona
        else:
            return ""
    @property
    def get_p3(self):
        if self.p3:
            return self.p3
        else:
            return ""
    @property
    def get_preferred_taxon(self):
        if self.subspecies:
            return f'{self.genus} {self.species} {self.subspecies}'
        elif self.species:
            return f'{self.genus} {self.species}'
        elif self.genus:
            return f'{self.genus}'
        elif self.tribe:
            return f'{self.tribe}'
        elif self.subfamily:
            return f'{self.subfamily}'
        elif self.family:
            return f'{self.family}'
        else:
            return f'{self.order}'
    @property
    def get_determiner(self):
        if self.determiner:
              return self.determiner
        else:
              return ""
    @property
    def get_determined_year(self):
        if self.determined_year:
              return self.determined_year
        else:
              return ""
#Specimen Functions
    @property
    def get_preparer(self):
        if self.preparer:
              return self.preparer
        else:
              return ""
    @property
    def get_prepared_date(self):
        if self.prepared_date:
              return self.prepared_date
        else:
              return ""
#Locality Functions
    @property
    def get_collecting_trip(self):
        if self.collecting_trip:
            return self.collecting_trip
        else:
            return ""
    @property
    def get_country(self):
        if self.country:
            return self.country
        else:
            return ""
    @property
    def get_state(self):
        if self.state:
            return self.state
        else:
            return ""
    @property
    def get_county(self):
        if self.county:
            return self.county
        else:
            return ""
    @property
    def get_locality(self):
        if self.locality:
            return self.locality
        else:
            return ""
    @property
    def get_gps(self):
        if self.gps:
            return self.gps
        else:
            return ""
    @property
    def get_date(self):
        if self.day and self.month and self.year:
            return f'{self.day} {self.month} {self.year}'
        elif self.month and self.year:
            return f'{self.month} {self.year}'
        elif self.year:
            return self.year
        else:
            return ""

    def display_collector(self):
        return ', '.join(collector.name for collector in self.collector.all()[:5])
#Method/Other Functions
    degree_sign= u'\N{DEGREE SIGN}'
    @property
    def get_weather(self):
        if self.weather:
            return self.weather
        else:
            return ""
    @property
    def get_temperatureC(self):
        if self.temperatureC:
            return f'{self.temperatureC}{self.degree_sign}C'
        else:
            return ""
    @property
    def get_temperatureF(self):
        if self.temperatureF:
            return f'{self.temperatureF}{self.degree_sign}F'
        else:
            return ""
    @property
    def get_time_of_day(self):
        if self.time_of_day:
            return self.time_of_day
        else:
            return ""
    @property
    def get_habitat_notes(self):
        if self.habitat_notes:
            return self.habitat_notes
        else:
            return ""
    @property
    def get_other_notes(self):
        if self.other_notes:
            return self.other_notes
        else:
            return ""
    def __str__(self):
        return f'{self.usi}'
    def get_absolute_url(self):
        return reverse('specimen-detail', args=[str(self.pk)])