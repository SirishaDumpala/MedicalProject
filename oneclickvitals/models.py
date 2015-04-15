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

class Appointment(models.Model):
    user = models.ForeignKey('auth.User')
    reason = models.CharField(max_length=50, null = True)
    phone_number = models.CharField(max_length=10, null = True)
    created_date = models.DateTimeField(
            default=timezone.now)
    appointment_date = models.DateField(
            blank=True, null=True)
    appointment_time = models.TimeField(
            blank=True, null=True)

    def __str__(self):
        return self.last_name

class PageAdmin(admin.ModelAdmin):

    list_display = ('last_name', 'phone_number')

    def __str__(self):
        return self.list_display

class UserDetail(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    phone_number = models.CharField(max_length=10, null = True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    insurance = models.CharField(max_length=50, null = True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class EmergencyContact(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    RELATIONSHIP_CHOICES =  (('parent', 'Parent'),('brother', 'Brother'),('sister', 'Sister'), ('boyfriend', 'Boyfriend'), ('girlfriend', 'Girlfriend'), ('other', 'Other'),)
    # The additional attributes we wish to include.
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES)
    phone_number = models.CharField(max_length=10, null = True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)


    def __str__(self):
        return self.user.username

class PatientMedicalHistory(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    HABIT_CHOICES = (('smoking', 'Smoking'),('alcohol', 'Alcohol'),('exercise', 'Exercise'),
                        ('street drugs', 'Street drugs'),)
    # The additional attributes we wish to include.
    allergies = models.TextField(max_length=100)
    current_medications = models.TextField(max_length=500)
    chief_complaint = models.TextField(max_length=500)
    surgical_history = models.TextField(max_length=500)
    medical_history = models.TextField(max_length=500)
    social_habits = models.CharField(max_length=50, choices=HABIT_CHOICES)


    def __str__(self):
        return self.user.username

    
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
    doctor_phone_number = models.CharField(max_length=10)
    doctor_address = models.CharField(max_length=100, blank=True)
    doctor_city = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return self.doctor_last_name

class PharmacyDetail(models.Model):
    pharmacy_name = models.CharField(max_length=50)
    pharmacy_address = models.CharField(max_length=100)
    pharmacy_city = models.CharField(max_length=50)
    pharmacy_phone_number = models.CharField(max_length=10)
    ncpdp_id = models.CharField(max_length=7)
    pharmacy_email = models.EmailField(max_length=75, blank=True, null=True)
    
    def __str__(self):
        return self.pharmacy_email
    
class Prescription(models.Model):
    DEFAULT_PK=1
    patient = models.ForeignKey(User, default=DEFAULT_PK)
    GENDER_CHOICES = (('male','Male'), ('female', 'Female'))
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    date_of_issuance = models.DateField(blank=True, null=True)
    day_supply = models.CharField(max_length=5, blank=True, null=True)
    drug_name = models.CharField(max_length=100, blank=True, null=True)
    drug_strength = models.CharField(max_length=5, blank=True, null=True)
    dosage_form = models.CharField(max_length=20, blank=True, null=True)
    FREQUENCY_CHOICES = (('daily','Daily',),('every other day','Every Other Day',),('Twice a Day','BID/b.i.d.',),('Three Times a Day','TID/t.id',), ('Four Times a Day','QID/q.i.d.',), ('Every Bedtime','QHS',), ('Every 4 Hours','Q4h',), ('Every 4 to 6 Hours','Q4-6h',), ('Every Week','QWK',),)
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES)
    quantity = models.CharField(max_length=6, blank=True, null=True)
    npi_number = models.CharField(max_length=10)
    ndc_number = models.CharField(max_length=11)
    REFILLS_CHOICES = (('yes', 'Yes',), ('no', 'No',),)
    refills = models.CharField(max_length=5, choices=REFILLS_CHOICES)
    
    def __str__(self):
        return self.drug_name