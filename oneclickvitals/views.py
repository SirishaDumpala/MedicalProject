from django.shortcuts import render, get_object_or_404, redirect, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse

from oneclickvitals.models import Appointment, PageAdmin, UserDetail, EmergencyContact, PatientMedicalHistory, Radiology, DoctorDetail, PharmacyDetail, Prescription, FamilyMedicalHistory, Diagnosis
from oneclickvitals.forms import UserForm, UserDetailForm, NewPatientForm, AppointmentForm, EmergencyContactForm, PatientMedicalHistoryForm, FamilyMedicalHistoryForm,DiagnosisForm, PatientRadiologyImageForm, DoctorDetailForm, PharmacyDetailForm, PrescriptionForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.context_processors import csrf
from django.contrib import auth
from medical_project.settings import MEDIA_URL, MEDIA_ROOT
from django.utils import timezone
from django.template import RequestContext
from django.contrib import messages
from medical_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, EmailMessage
import smtplib

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
        formE = FamilyMedicalHistoryForm(request.POST)

        if formA.is_valid() and formB.is_valid() and formC.is_valid() and formD.is_valid() and formE.is_valid():
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
            familyMedicalHistory = formE.save(commit = False)
            familyMedicalHistory.user = patientUser
            familyMedicalHistory.save()
            patientUser.groups.add(Group.objects.get(name='patient'))
            #print("saved new patient")

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
        formE = FamilyMedicalHistoryForm()

    # Render the form with error messages (if any), if no form supplied
    return render(request, 'oneclickvitals/add_newpatient.html', {'formA': formA, 'formB': formB, 'formC': formC, 'formD': formD, 'formE': formE})

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
    family_history = FamilyMedicalHistory.objects.get(user=me)
    diagnosis_info = Diagnosis.objects.filter(user=me)
    context_dict = {'profile':profile, 'emergency': emergency_contact, 'medical_history': medical_history, 'family_history': family_history,'diagnosis_info': diagnosis_info}
    print("in patient profile: ", diagnosis_info[0].date)
    return render(request, 'oneclickvitals/patient_profile.html', context_dict)

def patient_appointment_details(request):
    appointment_list = Appointment.objects.all()
    return render(request, 'oneclickvitals/patient_appointment_details.html', {'appointment': appointment_list})


def profile_edit(request, pk):
    profile = get_object_or_404(UserDetail, pk=pk)
    if request.method == "POST":
        form = UserDetailForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            #profile.author = request.user
            profile.save()
            return redirect('oneclickvitals.views.patient_profile', pk=profile.pk)
        else:
            print(form.errors)
    else:
        form = UserDetailForm(instance=profile)
    return render(request, 'oneclickvitals/edit_patient.html', {'form': form})


@login_required
def personal_profile(request):
    #me = User.objects.get(id=pk)
    me = request.user
    print (me.username)
    profile = UserDetail.objects.get(user=me)
    #profile_list = UserDetail.objects.all()
    emergency_contact= EmergencyContact.objects.get(user=me)
    medical_history = PatientMedicalHistory.objects.get(user=me)
    family_history = FamilyMedicalHistory.objects.get(user=me)
    diagnosis_info = Diagnosis.objects.filter(user=me)
    context_dict = {'profile':profile, 'emergency': emergency_contact, 'medical_history': medical_history,'family_history': family_history, 'diagnosis_info':diagnosis_info }
    print("in patient profile: ", profile.pharmacy_name)
    return render(request, 'oneclickvitals/personal_profile.html', context_dict)


def edit_patient(request, pk):
    if request.method == 'POST':
        formA = NewPatientForm(request.POST)
        formB = UserDetailForm(request.POST)
        formC = EmergencyContactForm(request.POST)
        formD = PatientMedicalHistoryForm(request.POST)
        formE = FamilyMedicalHistoryForm(request.POST)

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
            familyMedicalHistory = formE.save(commit = False)
            familyMedicalHistory.user = patientUser
            familyMedicalHistory.save()
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
        formE = FamilyMedicalHistoryForm()

    # Render the form with error messages (if any), if no form supplied
    return render(request, 'oneclickvitals/edit_patient.html', {'formA': formA, 'formB': formB, 'formC': formC, 'formD': formD, 'formE': formE})


def diagnosis(request):
    if request.method == 'POST':
        form = DiagnosisForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            diagnosis = form.save(commit=False)
            diagnosis.save()

            # The user will be shown the appointment detail page view.
            #return diagnosis_details(request)
            print ("Do I have the user id: ", diagnosis.pk)
            return diagnosis_details(request, diagnosis.pk)
        else:
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = DiagnosisForm()

    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/diagnosis.html', {'form': form})


def diagnosis_details(request, pk):
    #me = User.objects.get(id=pk)
    diagnosis_info = get_object_or_404(Diagnosis, pk=pk)
    return render(request, 'oneclickvitals/diagnosis_details.html', {'diagnosis_info': diagnosis_info})


def personal_diagnosis(request):
    me = request.user
    diagnosis_info = Diagnosis.objects.filter(user=me)
    return render(request, 'oneclickvitals/personal_diagnosis.html', {'diagnosis_info': diagnosis_info})

def patient_radiology_image(request):
    if request.method == 'POST':
        form = PatientRadiologyImageForm(request.POST, request.FILES)

        if form.is_valid():
            # Save the new image to the database.
            radiology_image = form.save(commit=False)
            radiology_image.save()

            # The user will be shown the radiology list.
            messages.success(request, 'Radiology image added.')
            #return redirect('radiology_list')
        else:
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
#            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = PatientRadiologyImageForm()
    
    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/add_radiology.html', {'form': form})

@login_required
def radiology_list(request):
    radiology_images = Radiology.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'oneclickvitals/radiology_list.html', {'radiology_images': radiology_images})


@login_required
def view_radiology(request, pk):
    img = get_object_or_404(Radiology, pk=pk)
    return render_to_response('oneclickvitals/view_radiology.html', {'img':img}, context_instance=RequestContext(request) )

@login_required
def edit_radiology(request, pk):
    img = get_object_or_404(Radiology, pk=pk)
    if request.method == 'POST':
        form = PatientRadiologyImageForm(request.POST, instance=img)

        if form.is_valid():
            # Save the new image to the database.
            radiology_image = form.save(commit=False)
            radiology_image.save()

            # The user will be shown the image list.
            return redirect('view_radiology', pk=img.pk)
        else:
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = PatientRadiologyImageForm(instance=img)

    # Render the form with error messages (if any)
    return render(request, 'oneclickvitals/edit_radiology.html', {'form': form})

@login_required
def add_prescription(request):
    if request.method == 'POST':
        formE = DoctorDetailForm(request.POST)
        formF = PharmacyDetailForm(request.POST)
        formG = PrescriptionForm(request.POST)
        #We use E, F, G, because the letters have not been used

        if formE.is_valid() and formF.is_valid() and formG.is_valid():
            doctorDetail = formE.save(commit=False)
            doctorDetail.save()
            pharmacyDetail = formF.save(commit=False)
            #doctorDetail.save()
            #pharmacyDetail.save()
            prescription = formG.save(commit=False)
            #doctorDetail.prescription = formG.save(commit=False)
            #doctorDetail.save()
            #prescription.doctor = doctorDetail
            prescription.save()

            messages.success(request, 'Prescription added.')
            #return redirect('prescription_list')
        else:
            messages.error(request, "Oops! You missed some fields. Please fill the required fields.")
    else:
        # If the request was not a POST, display the form to enter details.
        formE = DoctorDetailForm()
        formF = PharmacyDetailForm()
        formG = PrescriptionForm()

    # Render the form with error messages (if any), if no form supplied
    return render(request, 'oneclickvitals/add_prescription.html', {'formE': formE, 'formF': formF, 'formG': formG})

def prescription_list(request):
    prescription = Prescription.objects.all()
    return render(request, 'oneclickvitals/prescription_list.html', {'prescription': prescription})


def email_pharmacy(request, pk):
    doctors = DoctorDetail.objects.all()
    pharmacyInfo = PharmacyDetail()

    prescription = get_object_or_404(Prescription, pk=pk)

    subject = "New prescription"
    message = ""

    message += "\n" + str(doctors)

    message += "\n" + str(prescription)
    sender = EMAIL_HOST_USER
    recipient = ['bluishgrayfin@gmail.com']
    #recipient = [str(pharmacyInfo.pharmacy_email)]
    send_mail(subject, message, sender, recipient, fail_silently=False)
    return render_to_response('oneclickvitals/email_confirmation.html', context_instance=RequestContext(request) )
