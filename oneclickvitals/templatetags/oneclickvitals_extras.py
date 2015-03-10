from django import template
from oneclickvitals.models import Appointment, Newpatient

register = template.Library()

@register.inclusion_tag('oneclickvitals/appt.html')
def get_appointment_list():
    return {'appt': Appointment.objects.all()}

@register.inclusion_tag('oneclickvitals/pats.html')
def get_patient_list():
    return {'pats': Newpatient.objects.all()}
'''
@register.inclusion_tag('oneclickvitals/deets.html')
def get_details_list():
    return {'deets': Newpatient.objects.all()}
'''
