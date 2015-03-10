from django import forms
from django.contrib.auth.models import User
from oneclickvitals.models import Appointment, Newpatient, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('role',)

class NewPatientForm(forms.ModelForm):

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Newpatient
        fields = ('first_name','last_name','phone_number', 'date_of_birth', 'address', 'city',)

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('first_name','last_name','phone_number', 'reason', 'appointment_date',)
