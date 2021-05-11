from django.contrib import admin
from .models import VaccineType,Vaccine,VaccineGroups
# Register your models here.


admin.site.register(VaccineType)
admin.site.register(Vaccine)
admin.site.register(VaccineGroups)