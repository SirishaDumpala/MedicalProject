from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
from datetimewidget.widgets import DateWidget, DateTimeWidget, TimeWidget

class Appointment(models.Model):
    user = models.ForeignKey('auth.User')
    reason = models.CharField(max_length=50, null = True)
    created_date = models.DateTimeField(
            default=timezone.now)
    appointment_date = models.DateField(
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
    RELATIONSHIP_CHOICES =  (('parent', 'Parent'),('brother', 'Brother'),('sister', 'Sister'),
                                ('boyfriend', 'Boyfriend'), ('girlfriend', 'Girlfriend'), ('other', 'Other'),)
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
