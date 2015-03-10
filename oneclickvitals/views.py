from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from oneclickvitals.models import Newpatient, Appointment, PageAdmin
from oneclickvitals.forms import UserForm, UserProfileForm, NewPatientForm, AppointmentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):

    return render(request, 'oneclickvitals/index.html')

@login_required
def about(request):
    appointment_list = Appointment.objects.order_by('appointment_date')
    context_dict = {'appointments': appointment_list}
    return render(request, 'oneclickvitals/about.html', context_dict)

def add_newpatient(request):
    if request.method == 'POST':
        form = NewPatientForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            patient = form.save(commit=False)
            patient.author = request.user
            patient.save()

            # The user will be shown the patient profile page view.
            return patient_details(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = NewPatientForm()

    # Render the form with error messages (if any), if no form supplied
    return render(request, 'oneclickvitals/add_newpatient.html', {'form': form})

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            patient = form.save(commit=False)
            patient.author = request.user
            patient.save()

            # The user will be shown the appointment detail page view.
            return appointment_details(request)
        else:
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = AppointmentForm()
        
    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/appointment.html', {'form': form})

@login_required
def patient_details(request):
    details_list = Newpatient.objects.all()

    return render(request, 'oneclickvitals/patient_details.html', {'details': details_list})

@login_required
def appointment_details(request):
    appointment_list = Appointment.objects.all()
    return render(request, 'oneclickvitals/appointment_details.html', {'appointment': appointment_list})
