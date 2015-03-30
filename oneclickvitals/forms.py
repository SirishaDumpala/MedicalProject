from django import forms
from django.contrib.auth.models import User, Group
from oneclickvitals.models import Appointment,UserDetail
from datetimewidget.widgets import DateWidget, DateTimeWidget, TimeWidget

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ('insurance','phone_number','address','city')

class NewPatientForm(forms.ModelForm):

    class Meta:
        # Provide an association between the ModelForm and a model
        model = User
        fields = ('username','first_name','last_name','email', 'password', 'groups',)

class AppointmentForm(forms.ModelForm):

    #appointment_date = forms.DateTimeField(widget = DateTimeWidget(usel10n = True, bootstrap_version = 3))
    class Meta:
        model = Appointment
        widgets = {'appointment_date': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)}
        fields = ('user','reason', 'appointment_date',)
