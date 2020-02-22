from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from database.models import SpecimenRecord, SpecimenImage, SpeciesPage, CollectingTrip
from .filters import SpecimenRecordFilter, SpecimenImageFilter

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import ContactForm
from django.conf import settings

"""
STATIC VIEWS (HOME PAGE, ABOUT PAGE, SUCCESS PAGE, SITEMAP PAGE)
"""

class HomePage(TemplateView):
    template_name = 'database/templates/home.html'

def home(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_specimens = SpecimenRecord.objects.all().count()
    num_specimen_images = SpecimenImage.objects.all().count()
    num_species = SpeciesPage.objects.all().count()

    context = {
        'num_specimens': num_specimens,
        'num_specimen_images': num_specimen_images,
        'num_species': num_species,
    }

    # Render the HTML template home.html with the data in the context variable
    return render(request, 'home.html', context=context)

class AboutPage(TemplateView):
    template_name = 'database/templates/about.html'

def about(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = from_email
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    return render(request, 'about.html', {'form': form})

def success(request):
    return render(request, 'success.html')

class SiteMapPage(TemplateView):
    template_name = 'database/templates/sitemap.xml'

def sitemap(request):
    return render(request, 'sitemap.xml')

"""
SPECIMEN VIEWS (SPECIMEN LIST VIEW, SPECIMEN DETAIL VIEW, SPECIMEN FILTER, SPECIMEN IMAGE LIST VIEW)
"""
"""
class SpecimenListView(generic.ListView):
    model = SpecimenRecord
    paginate_by = 100
    template_name = 'database/templates/database/specimenrecord_list.html'

class SpecimenImagesListView(generic.ListView):
    model = SpecimenImage
    paginate_by = 200
    template_name = 'database/templates/database/specimenimage_list.html'
"""

class SpecimenDetailView(generic.DetailView):
    model = SpecimenRecord

class SpecimenRecordView(generic.ListView):
    model = SpecimenRecordFilter
    template_name = 'database/templates/database/specimenrecord_filter.html'

class SpecimenImageView(generic.ListView):
    model = SpecimenImageFilter
    template_name = 'database/templates/database/specimenimage_filter.html'

"""
SPECIES PAGE VIEWS (SPECIES PAGE LIST VIEW, SPECIES PAGE DETAIL VIEW)
"""

class SpeciesPageListView(generic.ListView):
    model = SpeciesPage
    template_name = 'database/templates/database/speciespage_list.html'

    def get_context_data(self, **kwargs):
        context = super(SpeciesPageListView, self).get_context_data(**kwargs)
        context['eudaminae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Eudaminae").order_by('species_name__species_p3')
        context['pyrginae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Pyrginae").order_by('species_name__species_p3')
        context['heteropterinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Heteropterinae").order_by('species_name__species_p3')
        context['hesperiinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Hesperiinae").order_by('species_name__species_p3')
        context['parnassiinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Parnassiinae").order_by('species_name__species_p3')
        context['papilioninae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Papilioninae").order_by('species_name__species_p3')
        context['coliadinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Coliadinae").order_by('species_name__species_p3')
        context['pierinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Pierinae").order_by('species_name__species_p3')
        context['miletinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Miletinae").order_by('species_name__species_p3')
        context['lycaeninae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Lycaeninae").order_by('species_name__species_p3')
        context['theclinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Theclinae").order_by('species_name__species_p3')
        context['polyommatinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Polyommatinae").order_by('species_name__species_p3')
        context['riodininae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Riodininae").order_by('species_name__species_p3')
        context['libytheinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Libytheinae").order_by('species_name__species_p3')
        context['danainae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Danainae").order_by('species_name__species_p3')
        context['heliconiinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Heliconiinae").order_by('species_name__species_p3')
        context['limenitidinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Limenitidinae").order_by('species_name__species_p3')
        context['apaturinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Apaturinae").order_by('species_name__species_p3')
        context['nymphalinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Nymphalinae").order_by('species_name__species_p3')
        context['charaxinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Charaxinae").order_by('species_name__species_p3')
        context['satyrinae_pages'] = SpeciesPage.objects.filter(species_name__genus__tribe__subfamily__subfamily_name="Satyrinae").order_by('species_name__species_p3')
        return context

class SpeciesPageDetailView(generic.DetailView):
    model = SpeciesPage

"""
COLLECTING TRIP VIEWS (COLLECTING TRIP LIST VIEW, COLLECTING TRIP DETAIL VIEW)
"""

class CollectingTripListView(generic.ListView):
    model = CollectingTrip
    paginate_by = 100

class CollectingTripDetailView(generic.DetailView):
    model = CollectingTrip
