from django.urls import path
from . import views
from django_filters.views import FilterView
from database.filters import SpecimenImageFilter

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('success/', views.success, name='success'),
    path('specimen-records/<str:pk>', views.specimen_detail, name='specimen-detail'),
    path('specimen-records/', views.specimen_filter, name='specimen-records'),
    path('specimen-images/', FilterView.as_view(filterset_class=SpecimenImageFilter), name='specimen-images'),
    path('species/', views.SpeciesPageListView.as_view(), name='species'),
    path('species/<str:pk>', views.SpeciesPageDetailView.as_view(), name='species-page'),
    path('collecting-trips/', views.CollectingTripListView.as_view(), name='collecting-trips'),
    path('collecting-trips/<str:pk>', views.CollectingTripDetailView.as_view(), name='collecting-trip-detail'),
    path('sitemap/', views.sitemap, name='sitemap'),
    ]