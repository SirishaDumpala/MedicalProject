from django import template
from oneclickvitals.models import Appointment, UserDetail

register = template.Library()

@register.inclusion_tag('oneclickvitals/appt.html')
def get_appointment_list():
    return {'appt': Appointment.objects.all()}

@register.inclusion_tag('oneclickvitals/pats.html')
def get_patient_list():
    return {'pats': UserDetail.objects.all()}
