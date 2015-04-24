from django import template
from oneclickvitals.models import *

register = template.Library()

@register.inclusion_tag('oneclickvitals/appt.html')
def get_appointment_list():
    return {'appt': Appointment.objects.all()}

@register.inclusion_tag('oneclickvitals/pats.html')
def get_patient_list():
    return {'pats': UserDetail.objects.all()}

@register.inclusion_tag('oneclickvitals/rad_img.html')
def get_radiology_list():
    return {'rad_img': Radiology.objects.all()}

@register.inclusion_tag('oneclickvitals/pres.html')
def get_prescription_list():
    return {'pres': Prescription.objects.all()}

@register.inclusion_tag('oneclickvitals/diag.html')
def get_visit_records():
    return {'diag': Diagnosis.objects.all()}
