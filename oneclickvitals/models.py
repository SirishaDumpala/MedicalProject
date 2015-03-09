from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User


class Newpatient(models.Model):
    author = models.ForeignKey('auth.User')
    first_name = models.CharField(max_length=15, null = True)
    last_name = models.CharField(max_length=15, null = True)
    phone_number = models.CharField(max_length=10, null = True)
    date_of_birth = models.DateField(max_length=8)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    '''
    #registration_date = models.DateTimeField(
            blank=True, null=True)
    #patient_name = models.CharField(max_length=15)
    #phone_numer = models.PhoneNumberField()
    '''

    def confirm_newpatient(self): #function for confirming new patient registration
        self.newpatient_date = timezone.now()
        self.save()

    def __str__(self):
        return self.last_name


class Appointment(models.Model):
    author = models.ForeignKey('auth.User')
    first_name = models.CharField(max_length=15, null = True)
    last_name = models.CharField(max_length=15, null = True)
    phone_number = models.CharField(max_length=10, null = True)
    #patient_name = models.CharField(max_length=15)
    #phone_numer = models.PhoneNumberField()
    reason = models.TextField()
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

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    role = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.user.username
