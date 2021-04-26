from django.db import models
from django.conf import settings
from slugify import slugify
from django.urls import reverse


class Bed(models.Model):
    """ The Patient class defines the main storage point for Beds. """

    bed_choices = [
        ('General', 'General'),
        ('Semi-Private', 'Semi-Private'),
        ('Private', 'Private')
    ]
    bed_type = models.CharField(
        max_length=100, choices=bed_choices, default="General")

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + '. ' + self.bed_type

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)


class Patient(models.Model):
    """ The Patient class defines the main storage point for Patients. """

    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    name = models.CharField(max_length=100)
    gender = models.CharField('Gender', max_length=100,
                              choices=gender_choices, null=True, blank=True)
    email = models.EmailField('Email address', null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bed = models.ForeignKey(
        Bed, on_delete=models.SET_NULL, null=True, default=None)
    checked_out = models.BooleanField('Check out', default=False)
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('Patient-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        patient_name = self.name
        self.slug = slugify(patient_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
