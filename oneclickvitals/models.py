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

    def __str__(self):
        return self.user.username
