from django.contrib import admin
from oneclickvitals.models import Newpatient, Appointment, PageAdmin
from oneclickvitals.models import UserProfile

admin.site.register(Newpatient, PageAdmin)
admin.site.register(Appointment, PageAdmin)
admin.site.register(UserProfile)
