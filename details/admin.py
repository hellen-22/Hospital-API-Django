from django.contrib import admin
from .models import *


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Pharmacy)
admin.site.register(Lab)
admin.site.register(Speciality)
admin.site.register(Nurse)
admin.site.register(DoctorAvailability)
admin.site.register(PatientConsultation)