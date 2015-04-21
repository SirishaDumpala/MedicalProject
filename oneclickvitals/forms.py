from django import forms
from django.contrib.auth.models import User, Group

from oneclickvitals.models import LabTest, Pharmacy, Appointment,UserDetail, EmergencyContact, PatientMedicalHistory, FamilyMedicalHistory, Diagnosis, Radiology, DoctorDetail, Prescription
from datetimewidget.widgets import DateWidget, DateTimeWidget, TimeWidget
from django.utils.safestring import mark_safe

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        #widgets = {'date_of_birth': DateWidget(attrs={'id':"yourdateid"}, usel10n = True, bootstrap_version=3)}
        fields = ('pharmacy_name','pharmacy_phone_number','address_1','address_2','city','state','zip_code',)


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail

        fields = ('gender','date_of_birth','insurance','phone_number','address_1','address_2','city','state','zip_code',)


class NewPatientForm(forms.ModelForm):

    class Meta:
        # Provide an association between the ModelForm and a model
        model = User
        fields = ('first_name','last_name','username','email', 'groups',)

class AppointmentForm(forms.ModelForm):

    #appointment_date = forms.DateTimeField(widget = DateTimeWidget(usel10n = True, bootstrap_version = 3))
    class Meta:
        model = Appointment

        widgets = {'appointment_date': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
                  'appointment_time': TimeWidget(attrs= {'id':"yourtimeid"}, usel10n = True, bootstrap_version=3)}
        fields = ('user','type_of_appointment', 'reason_for_appointment', 'phone_number','appointment_date','appointment_time',)


class EmergencyContactForm(forms.ModelForm):

    class Meta:
        # Provide an association between the ModelForm and a model
        model = EmergencyContact
        fields = ('contact_first_name','contact_last_name','relationship', 'contact_phone_number','address_1','address_2','city','state','zip_code',)

class PatientMedicalHistoryForm(forms.ModelForm):

    class Meta:
        # Provide an association between the ModelForm and a model
        model = PatientMedicalHistory
        fields = ('height','weight','blood_type','allergies','current_medications','chief_complaint', 'surgical_history', 'medical_history','social_habits',)


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class FamilyMedicalHistoryForm(forms.ModelForm):

    class Meta:
        # Provide an association between the ModelForm and a model
        model = FamilyMedicalHistory
        widgets = {'stroke': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'cancer': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'high_bp': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'tuberculosis': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'diabetes': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'leukemia': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'bleeding_tendency': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'heart_attack': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'kidney_disease': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'rheumatic_heart': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'heart_failure': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    }
        fields = ('stroke','cancer','high_bp', 'tuberculosis', 'diabetes', 'leukemia', 'bleeding_tendency', 'heart_attack','kidney_disease', 'rheumatic_heart', 'heart_failure',)

class DiagnosisForm(forms.ModelForm):

    #appointment_date = forms.DateTimeField(widget = DateTimeWidget(usel10n = True, bootstrap_version = 3))
    class Meta:
        model = Diagnosis
        widgets = {'date': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
                    'follow_up': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'lab_test': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),}

        fields = ('user', 'date','complaint', 'diagnosis','additional_comments','follow_up', 'lab_test',)


class LabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        widgets = {'urine_culture': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'blood_culture': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'blood_glucose': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'allergy_test': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'thyroid': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'viral_test': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'pregnancy_test': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),}
        fields = ('urine_culture', 'blood_culture', 'blood_glucose', 'allergy_test', 'thyroid', 'viral_test', 'pregnancy_test', 'x_ray',)

class PatientRadiologyImageForm(forms.ModelForm):

    class Meta:
        model = Radiology
        widgets = {'created_date': DateWidget(attrs={'id':"yourcreateddateid"}, usel10n = True, bootstrap_version=3)}
        fields = ('user', 'title', 'created_date', 'caption', 'image',)


class DoctorDetailForm(forms.ModelForm):
    class Meta:
        model = DoctorDetail
        fields = ('doctor_first_name', 'doctor_last_name', 'name_suffix', 'prescription_network_id', 'dea', 'doctor_phone_number', 'address_1','address_2', 'city','state','zip_code')

'''
class PharmacyDetailForm(forms.ModelForm):
    class Meta:
        model = PharmacyDetail
        fields = ('pharmacy_name', 'pharmacy_address', 'pharmacy_city', 'pharmacy_phone_number', 'ncpdp_id','pharmacy_email',)
'''

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        widgets = {'refills': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))) }
        #widgets = {
        #    'date_of_issuance': DateWidget(attrs={'id':"yourissuancedate"}, usel10n = True, bootstrap_version=3)}
        fields = ('user', 'gender', 'date_of_issuance', 'days_supply', 'drug_name', 'drug_strength', 'dosage_form', 'frequency', 'quantity', 'npi_number', 'ndc_number', 'refills')
'''
class SummaryForm(forms.ModelForm):

    class Meta:
        # Provide an association between the ModelForm and a model
        model = UserDetail
        fields = ('user',)
'''
