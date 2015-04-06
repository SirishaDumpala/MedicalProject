from django.contrib import admin
from oneclickvitals.models import Appointment, UserDetail

admin.site.register(Appointment)
admin.site.register(UserDetail)

#from myagenda.calendars import Calendar
#from myagenda.events import  Event
#from myagenda.models import MyCalendar, MyEvent

#admin.site.unregister(Calendar)
#admin.site.register(MyCalendar, admin.ModelAdmin)
#
#admin.site.unregister(Event)
#admin.site.register(MyEvent, admin.ModelAdmin)