from django.conf.urls import patterns, url
from oneclickvitals import views
from django.conf import settings
from django.conf.urls.static import static
from oneclickvitals.views import view_radiology
from medical_project.settings import MEDIA_ROOT

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^add_newpatient/$', views.add_newpatient, name='add_newpatient'),
        url(r'^appointment/$', views.appointment, name='appointment'),
        url(r'^patient_details/$', views.patient_details, name='patient_details'),
        url(r'^appointment_details/$', views.appointment_details, name='appointment_details'),
        url(r'^patient_appointment_details/$', views.patient_appointment_details, name='patient_appointment_details'),
        url(r'^add_radiology/$', views.patient_radiology_image, name='patient_radiology_image'),
        url(r'^radiology_list/$', views.radiology_list, name='radiology_list'),
        url(r'^view_radiology/(?P<pk>[0-9]+)/$', views.view_radiology, name='view_radiology'),
        url(r'^view_radiology/(?P<pk>[0-9]+)/edit/$', views.edit_radiology, name='edit_radiology'),
        url(r'^add_prescription/$', views.add_prescription, name='add_prescription'),
        url(r'^prescription_list/$', views.prescription_list, name='prescription_list'),
        url(r'^email_confirmation/(?P<pk>[0-9]+)/$', views.email_pharmacy, name='email_confirmation'),
                      )

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
