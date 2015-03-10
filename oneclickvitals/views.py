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
    # A HTTP POST?
    if request.method == 'POST':
        form = NewPatientForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            patient = form.save(commit=False)
            patient.author = request.user
            patient.save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        print ('Not a post request about to call')
        form = NewPatientForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/add_newpatient.html', {'form': form})

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            patient = form.save(commit=False)
            patient.author = request.user
            patient.save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = AppointmentForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/appointment.html', {'form': form})

@login_required
def patient_details(request):
    details_list = Newpatient.objects.all()

    return render(request, 'oneclickvitals/patient_details.html', {'details': details_list})

@login_required
def appointment_detail(request):
    appointment = get_object_or_404(Appointment)
    return render(request, 'oneclickvitals/appointment_detail.html', {'appointment': appointment})
