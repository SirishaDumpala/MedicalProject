from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
from datetimewidget.widgets import DateWidget, DateTimeWidget, TimeWidget

class Appointment(models.Model):
    user = models.ForeignKey('auth.User')
    reason = models.CharField(max_length=50, null = True)
    phone_number = models.CharField(max_length=10, null = True)
    created_date = models.DateTimeField(
            default=timezone.now)
    appointment_date = models.DateTimeField(
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
    GENDER_CHOICES = (('female', 'Female',), ('male', 'Male',))

    # The additional attributes we wish to include.
    phone_number = models.CharField(max_length=10, null = True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    insurance = models.CharField(max_length=50, null = True)
    pharmacy_name = models.CharField(max_length=50, null = True)
    pharmacy_address = models.CharField(max_length=50, null = True)
    pharmacy_phone_number = models.CharField(max_length=10, null = True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null = True)

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
    contact_phone_number = models.CharField(max_length=10, null = True)
    contact_address = models.CharField(max_length=100, null = True)
    contact_city = models.CharField(max_length=50, null = True)


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
