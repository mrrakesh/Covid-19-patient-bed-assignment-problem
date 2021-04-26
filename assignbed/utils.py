from .models import Patient, Bed


def get_patient(bed_type):
    try:
        beds = Bed.objects.filter(bed_type=bed_type)
        patients = {}
        for bed in beds:
            patient = Patient.objects.filter(bed=bed, checked_out=False).get()
            patients[patient.id] = {
                'bed_type': bed_type,
                'name': patient.name,
                'gender': patient.gender,
                'email': patient.email,
                'address': patient.address
            }

        return patients
    except Exception as ex:
        print(ex)


def get_status_of_available_beds(bed_type):
    try:
        beds = Bed.objects.filter(bed_type=bed_type, is_available=True)
        if beds:
            no_of_beds = beds.count()
            return f"Total number of available beds of type {bed_type} are {no_of_beds}"
        else:
            return "Not avilable"
    except Exception as ex:
        print(ex)


def available_beds():
    try:
        beds = Bed.objects.filter(is_available=True)
        available_beds = {}
        for bed in beds:
            available_beds[bed.id] = {
                'bed_number': bed.id,
                'bed_type': bed.bed_type
            }

        return available_beds

    except Exception as ex:
        print(ex)
