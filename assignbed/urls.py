from .views import (
    PatientListView,
    PatientDetailView,
    PatientCreateView,
    PatientCheckoutView,
    BedListView,
    BedCreateView,
    BedDetailView,
)
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Patient list
    path('', PatientListView.as_view(), name='patient-list'),

    # Patient detail page
    path('patient/<int:pk>/<slug:slug>',
         PatientDetailView.as_view(), name='patient-detail'),

    # Create new Patient page
    path('patient/new', PatientCreateView.as_view(), name='patient-create'),

    # Patient checkout page
    path('patient/checkout/<int:pk>',
         PatientCheckoutView.as_view(), name='patient-checkout'),

    # Bed list
    path('bed', BedListView.as_view(), name='bed-list'),

    # Add new bed
    path('bed/new', BedCreateView.as_view(), name='bed-create'),

    # Bed detail page
    path('bed/<int:pk>',
         BedDetailView.as_view(), name='bed-detail'),

]
