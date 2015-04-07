from django.conf.urls import patterns, url
from oneclickvitals import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^add_newpatient/$', views.add_newpatient, name='add_newpatient'),
        url(r'^appointment/$', views.appointment, name='appointment'),
        url(r'^patient_details/$', views.patient_details, name='patient_details'),
        url(r'^appointment_details/$', views.appointment_details, name='appointment_details'),
        url(r'^patient_appointment_details/$', views.patient_appointment_details, name='patient_appointment_details'),
        url(r'^add_radiology/$', views.add_radiology, name='add_radiology'),
        )
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
