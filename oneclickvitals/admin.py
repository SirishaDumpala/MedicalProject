from django.contrib import admin
from oneclickvitals.models import Appointment, UserDetail
#from .models import UploadedImage

admin.site.register(Appointment)
admin.site.register(UserDetail)
#admin.site.register(UploadedImage, UploadedImageAdmin)


#class UploadedImageAdmin(admin.ModelAdmin):
#    pass

