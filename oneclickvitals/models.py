from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
from datetimewidget.widgets import DateWidget, DateTimeWidget, TimeWidget
from django.core.urlresolvers import reverse
from django.core.files import File
from os.path import join as pjoin
from tempfile import *
from PIL import Image as PImage
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _
from django_localflavor_us.models import USStateField



class Appointment(models.Model):
    user = models.ForeignKey('auth.User')
    APPOINTMENT_CHOICES = (('routine_preventive_care', 'Routine Preventive Care',),
                            ('follow_up', 'Follow-Up',),
                            ('routine_problem_visit', 'Routine Problem Visit'),
                            ('urgent_same_day_appointment', 'Urgent/Same Day Appointment'),
                            ('nurse_visit', 'Nurse Visit'),
                            ('allergy_shots', 'Allergy Shots'),
                            ('new_patients_and_referrals', 'New Patients and Referrals'),)
    type_of_appointment = models.CharField(max_length=100, choices=APPOINTMENT_CHOICES, null = True)
    reason_for_appointment = models.CharField(max_length=50, null = True)
    phone_number = models.CharField(max_length=10, null = True)
    created_date = models.DateTimeField(
            default=timezone.now)
    appointment_date = models.DateTimeField(
            blank=True, null=True)
    appointment_time = models.TimeField(
            blank=True, null=True)
    #cancel = models.NullBooleanField()

    def __str__(self):
        return self.last_name

class PageAdmin(admin.ModelAdmin):

    list_display = ('last_name', 'phone_number')

    def __str__(self):
        return self.list_display

class UserDetail(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    GENDER_CHOICES = (('female', 'Female',), ('male', 'Male',))
    # The additional attributes we wish to include.

    phone_number = models.CharField(max_length=14, null = True)
    address_1 = models.CharField(_("address"), max_length=128, blank = True)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64, default="Fullerton")
    state = USStateField(_("state"), default="CA")
    zip_code = models.CharField(_("zip code"), max_length=5, default= '92614')
    insurance = models.CharField(max_length=50, null = True)
    date_of_birth = models.CharField(max_length=10, null = True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null = True)

    def __str__(self):
        return self.user.username

class Pharmacy(models.Model):
    user = models.OneToOneField(User)
    pharmacy_name = models.CharField(max_length=50, null = True)
    pharmacy_phone_number = models.CharField(max_length=14, null = True)
    address_1 = models.CharField(_("address"), max_length=128, blank = True)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64, default="Fullerton")
    state = USStateField(_("state"), default="CA")
    zip_code = models.CharField(_("zip code"), max_length=5, default= '92614')

    def __str__(self):
        return self.user.username


class EmergencyContact(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    RELATIONSHIP_CHOICES =  (('spouse', 'Spouse'),('parent', 'Parent'),('brother', 'Brother'),('sister', 'Sister'), ('boyfriend', 'Boyfriend'), ('girlfriend', 'Girlfriend'), ('other', 'Other'),)
    # The additional attributes we wish to include.
    contact_first_name = models.CharField(max_length=50, null = True)
    contact_last_name = models.CharField(max_length=50, null = True)
    relationship = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES, null = True)
    contact_phone_number = models.CharField(max_length=14, null = True)
    address_1 = models.CharField(_("address"), max_length=128, blank = True)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64, default="Fullerton")
    state = USStateField(_("state"), default="CA")
    zip_code = models.CharField(_("zip code"), max_length=5, default= '92614')
    #contact_address = models.CharField(max_length=100, null = True)
    #contact_city = models.CharField(max_length=50, null = True)


    def __str__(self):
        return self.user.username

class PatientMedicalHistory(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    HABIT_CHOICES = (('smoking', 'Smoking'),('alcohol', 'Alcohol'),('exercise', 'Exercise'),
                        ('street drugs', 'Street Drugs'),('other', 'Other'),('none', 'None'))
    # The additional attributes we wish to include.
    height = models.PositiveIntegerField(max_length=5, null = True)
    weight = models.FloatField(max_length=10, null = True)
    blood_type = models.CharField(max_length=4, null = True)
    allergies = models.TextField(max_length=100)
    current_medications = models.TextField(max_length=500)
    chief_complaint = models.TextField(max_length=500)
    #surgery = models.BooleanField(initial=False)
    surgical_history = models.TextField(max_length=500)
    medical_history = models.TextField(max_length=500)
    social_habits = models.CharField(max_length=50, choices=HABIT_CHOICES)


    def __str__(self):
        return self.user.username



class FamilyMedicalHistory(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    stroke = models.NullBooleanField()
    cancer = models.NullBooleanField()
    high_bp = models.NullBooleanField()
    tuberculosis = models.NullBooleanField()
    diabetes = models.NullBooleanField()
    leukemia = models.NullBooleanField()
    bleeding_tendency = models.NullBooleanField()
    heart_attack = models.NullBooleanField()
    kidney_disease = models.NullBooleanField()
    rheumatic_heart = models.NullBooleanField()
    heart_failure = models.NullBooleanField()


    def __str__(self):
        return self.user.username

class Diagnosis(models.Model):
    user = models.ForeignKey('auth.User')
    date = models.DateField(default=timezone.now)
    complaint = models.TextField(max_length=500)
    diagnosis = models.TextField(max_length=500, null=True)
    follow_up = models.NullBooleanField()
    additional_comments = models.TextField(max_length=500)
    lab_test = models.NullBooleanField()


    def __str__(self):
        return self.last_name


class LabTest(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.ForeignKey('auth.User')
    XRAY_CHOICES = (('finger', 'Finger'),('palm', 'Palm'),('wrist', 'Wrist'),
                    ('right elbow', 'Right Elbow'),('left elbow', 'Left Elbow'),
                    ('right shoulder', 'Right Shoulder'),('neck', 'Neck'),('upper back', 'Upper Back'),
                    ('middle back', 'Middle Back'),('lower back', 'Lower Back'),
                    ('right knee', 'Right Knee'),('left knee', 'Left Knee'),
                    ('right leg', 'Right leg'),('left leg', 'Left Leg'),
                    ('right ankle', 'Right Ankle'), ('left ankle', 'Left Ankle'),
                    ('right foot', 'Right Foot'),('left foot', 'Left Foot'),('other', 'Other'), ('none', 'None'),)
    # The additional attributes we wish to include.
    urine_culture = models.NullBooleanField()
    blood_culture = models.NullBooleanField()
    allergy_test = models.NullBooleanField()
    blood_glucose = models.NullBooleanField()
    thyroid = models.NullBooleanField()
    viral_test = models.NullBooleanField()
    pregnancy_test = models.NullBooleanField()
    x_ray = models.CharField(max_length=50, choices=XRAY_CHOICES)


    def __str__(self):
        return self.last_name



'''
class LabTestOrder(models.Model):
    user = models.ForeignKey('auth.User')
    TEST_CHOICES = (('urine_culture', 'Urine Culture'),
              ('blood_culture', 'Blood Culture'),
              ('allergy_test', 'Allergy Test'),
              ('blood_glucose', 'Blood Glucose'),
              ('blood_type', 'Blood Type'),
              ('thyroid', 'Thyroid'),
              ('viral_test', 'Viral Test'),
              ('pregnancy_test', 'Pregnancy Test'))
    type_of_test = models.MultipleChoiceField(choices=TEST_CHOICES)

    def __str__(self):
        return self.last_name
'''


class Radiology(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=60, blank=True)
    image = models.ImageField(upload_to='image')
    created_date = models.DateField(blank=True, null=True)
    caption = models.CharField(max_length=60, blank=True)


    def __str__(self):
        return self.user.last_name

class DoctorDetail(models.Model):
    # This line is required. Links UserProfile to a User model instance.

    doctor_first_name = models.CharField(max_length=50)
    doctor_last_name = models.CharField(max_length=50)
    name_suffix = models.CharField(max_length=10)
    prescription_network_id = models.CharField(max_length=13)
    dea = models.CharField(max_length=8)
    doctor_phone_number = models.CharField(max_length=14, default= '(717) 444-0880' )
    address_1 = models.CharField(_("address"), max_length=128, default="Grand Pasteur Clinic")
    address_2 = models.CharField(_("address cont'd"), max_length=128, default="515 Hamilton Ave")
    city = models.CharField(_("city"), max_length=64, default="Fullerton")
    state = USStateField(_("state"), default="CA")
    zip_code = models.CharField(_("zip code"), max_length=5, default= '92652')


    def __str__(self):
        return self.doctor_last_name
'''
class PharmacyDetail(models.Model):
    pharmacy_name = models.CharField(max_length=50)
    pharmacy_address = models.CharField(max_length=100)
    pharmacy_city = models.CharField(max_length=50)
    pharmacy_phone_number = models.CharField(max_length=10)
    ncpdp_id = models.CharField(max_length=7)
    pharmacy_email = models.EmailField(max_length=75, blank=True, null=True)

    def __str__(self):
        return self.pharmacy_email
'''

class Prescription(models.Model):
    #DEFAULT_PK=1
    user = models.ForeignKey('auth.User')
    FREQUENCY_CHOICES = (('daily','Daily',),('every other day','Every Other Day',),('Twice a Day','BID/b.i.d.',),('Three Times a Day','TID/t.id',), ('Four Times a Day','QID/q.i.d.',), ('Every Bedtime','QHS',), ('Every 4 Hours','Q4h',), ('Every 4 to 6 Hours','Q4-6h',), ('Every Week','QWK',),)
    GENDER_CHOICES = (('male','Male'), ('female', 'Female'))
    #REFILLS_CHOICES = (('yes', 'Yes',), ('no', 'No',),)
    #patient = models.ForeignKey('auth.User')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    date_of_issuance = models.CharField(max_length=10, null = True)
    days_supply = models.CharField(max_length=5, blank=True, null=True)
    drug_name = models.CharField(max_length=100, blank=True, null=True)
    drug_strength = models.CharField(max_length=5, blank=True, null=True)
    dosage_form = models.CharField(max_length=20, blank=True, null=True)
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES)
    quantity = models.CharField(max_length=6, blank=True, null=True)
    npi_number = models.CharField(max_length=10)
    ndc_number = models.CharField(max_length=11)
    refills = models.NullBooleanField()

    def __str__(self):
        return self.drug_name
