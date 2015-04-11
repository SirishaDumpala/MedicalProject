from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from oneclickvitals.models import Appointment, PageAdmin, UserDetail, EmergencyContact, PatientMedicalHistory
from oneclickvitals.forms import UserForm, UserDetailForm, NewPatientForm, AppointmentForm, EmergencyContactForm, PatientMedicalHistoryForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.context_processors import csrf
from django.contrib import auth


def is_patient(user):
    return user.groups.filter(name="patient").exists()

def is_doctor(user):
    return user.groups.filter(name="doctor").exists()

def is_staff(user):
    return user.groups.filter(name="staff").exists()


def index(request):
    return render(request, 'index.html')

def index_patient(request):
    return render(request, 'index_patient.html')

def index_doctor(request):
    return render(request, 'index_doctor.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:

            if user.groups.filter(name="patient").exists():
                # Correct password, and the user is marked "active"
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect("/patient/")
            else:
                # Correct password, and the user is marked "active"
                login(request, user)
                return HttpResponseRedirect("/oneclickvitals/")
        else:
            return render(request, "registration/invalid_login.html")
    else:
        return render(request, 'registration/login.html')

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return render(request, 'registration/logout.html')

def invalid_login_view(request):
    if not user.is_authenticated():
         return render(request, 'registration/invalid_login.html')

@login_required
def about(request):
    appointment_list = Appointment.objects.order_by('appointment_date')
    context_dict = {'appointments': appointment_list}
    return render(request, '/about.html', context_dict)

def add_newpatient(request):
    if request.method == 'POST':
        formA = NewPatientForm(request.POST)
        formB = UserDetailForm(request.POST)
        formC = EmergencyContactForm(request.POST)
        formD = PatientMedicalHistoryForm(request.POST)

        if formA.is_valid() and formB.is_valid() and formC.is_valid():
            # Save the new category to the database.
            patientUser = formA.save()
            patientInfo = formB.save(commit=False)
            patientInfo.user = patientUser
            patientInfo.save()
            emergencyContact = formC.save(commit = False)
            emergencyContact.user = patientUser
            emergencyContact.save()
            patientMedicalHistory = formD.save(commit = False)
            patientMedicalHistory.user = patientUser
            patientMedicalHistory.save()
            patientUser.groups.add(Group.objects.get(name='patient'))
            print("saved new patient")

            # The user will be shown the patient profile page view.
            return patient_details(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(formA.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formA = NewPatientForm()
        formB = UserDetailForm()
        formC = EmergencyContactForm()
        formD = PatientMedicalHistoryForm()

    # Render the form with error messages (if any), if no form supplied
    return render(request, 'oneclickvitals/add_newpatient.html', {'formA': formA, 'formB': formB, 'formC': formC, 'formD': formD})

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            appointment = form.save(commit=False)
            appointment.save()

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
    details_list = UserDetail.objects.all()

    return render(request, 'oneclickvitals/patient_details.html', {'details': details_list})

@login_required
def appointment_details(request):
    appointment_list = Appointment.objects.all()
    return render(request, 'oneclickvitals/appointment_details.html', {'appointment': appointment_list})

@login_required
def patient_profile(request, pk):
    me = User.objects.get(id=pk)
    profile = UserDetail.objects.get(user=me)
    #profile_list = UserDetail.objects.all()
    emergency_contact= EmergencyContact.objects.get(user=me)
    medical_history = PatientMedicalHistory.objects.get(user=me)
    context_dict = {'profile':profile, 'emergency': emergency_contact, 'medical_history': medical_history}
    print("in patient profile: ", me.username)
    return render(request, 'oneclickvitals/patient_profile.html', context_dict)

def patient_appointment_details(request):
    appointment_list = Appointment.objects.all()
    return render(request, 'oneclickvitals/patient_appointment_details.html', {'appointment': appointment_list})

@login_required
def add_radiology(request):
    return render(request, 'oneclickvitals/add_radiology.html')

def profile_edit(request, pk):
    profile = get_object_or_404(UserDetail, pk=pk)
    if request.method == "POST":
        form = UserDetailForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.author = request.user
            profile.save()
            return redirect('oneclickvitals.views.patient_profile', pk=user.pk)
    else:
        form = UserDetailForm(instance=profile)
    return render(request, 'oneclickvitals/add_newpatient.html', {'form': form})


@login_required
def personal_profile(request):
    #me = User.objects.get(id=pk)
    me = request.user
    print (me.username)
    profile = UserDetail.objects.get(user=me)
    #profile_list = UserDetail.objects.all()
    emergency_contact= EmergencyContact.objects.get(user=me)
    medical_history = PatientMedicalHistory.objects.get(user=me)
    context_dict = {'profile':profile, 'emergency': emergency_contact, 'medical_history': medical_history}
    print("in patient profile: ", me.username)
    return render(request, 'oneclickvitals/personal_profile.html', context_dict)
