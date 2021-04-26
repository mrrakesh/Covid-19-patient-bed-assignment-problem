from django import forms
from .models import Bed


class BedForm(forms.Form):
    """
    Bed form to add new bed.
    Below are the constraints for the type of beds:
    1. general(50%) - index (0,2,4) 
    2. semi-private(25%) - index (1,5,9) 
    3. private(25%) - index (3,7,11) 

    """

    if Bed.objects.last():
        id = Bed.objects.last().id + 1
    else:
        id = 1

    bed_type = None
    if id % 2 == 0:
        bed_type = 'General'
    elif id % 4 == 1:
        bed_type = 'Semi-Private'
    else:
        bed_type = 'Private'

    id = forms.IntegerField(
        label='Bed Number', initial=id, disabled=True)
    bed_type = forms.CharField(
        label='Bed Type', initial=bed_type, disabled=True)
