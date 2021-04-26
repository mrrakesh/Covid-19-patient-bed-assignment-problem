from .models import Patient, Bed
from django.views import generic
from django.urls import reverse
from .forms import BedForm
from django.shortcuts import redirect
from django.contrib import messages


class PatientListView(generic.ListView):
    """View to list all of the patients."""

    model = Patient
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['page_title'] = 'Home'

        return context


class PatientDetailView(generic.DetailView):
    """View to display detail of a patient."""

    model = Patient


class PatientCreateView(generic.CreateView):
    """View to create a patients."""

    model = Patient
    fields = ['name', 'bed', 'gender', 'email', 'address']

    def form_valid(self, form):
        if Bed.objects.get(id=form.cleaned_data.get(
                'bed').id).is_available:
            bed = Bed.objects.filter(id=form.cleaned_data.get(
                'bed').id).update(is_available=False)
            messages.add_message(self.request, messages.SUCCESS,
                                 'Patient added successfully.')
            return super().form_valid(form)
        else:
            messages.add_message(self.request, messages.ERROR,
                                 'The selected bed is not available as of now.')
            return redirect(('patient-create'))

    success_url = '/'


class PatientCheckoutView(generic.UpdateView):

    """View to checkout for a patient."""

    model = Patient
    fields = ['name', 'bed', 'checked_out']

    def form_valid(self, form):
        if form.cleaned_data.get('checked_out'):
            Bed.objects.filter(id=form.cleaned_data.get(
                'bed').id).update(is_available=True)
        messages.add_message(self.request, messages.SUCCESS,
                             'The patient is successfully checked out.')
        return super().form_valid(form)

    success_url = '/'


class BedListView(generic.ListView):
    """View to list all of the beds."""

    model = Bed
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['page_title'] = 'Bed List'

        return context


class BedCreateView(generic.FormView):
    """View to add  a bed."""

    model = Bed
    form_class = BedForm

    template_name = 'assignbed/bed_form.html'

    def form_valid(self, form):
        bed = Bed(
            id=form.cleaned_data.get('id'),
            bed_type=form.cleaned_data.get('bed_type'),
            is_available=True
        )

        bed.save()
        messages.add_message(self.request, messages.SUCCESS,
                             'The bed is added successfully.')
        return redirect('bed-list')

    success_url = '/'


class BedDetailView(generic.ListView):
    """View to display details of a bed."""

    model = Bed
    template_name = 'assignbed/bed_detail.html'

    def get_queryset(self):
        bed_id = self.kwargs['pk']
        self.patient_obj = Patient.objects.filter(bed=bed_id)
        self.bed_obj = Bed.objects.filter(id=bed_id)

        return self.patient_obj, self.bed_obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.bed_obj:
            context['bed_obj'] = self.bed_obj
        if self.patient_obj:
            context['patient_obj'] = self.patient_obj

        return context
