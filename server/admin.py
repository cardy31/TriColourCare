from django.contrib import admin
from .models import Patient, Doctor, Comment, DietSuggestion, DietRestriction, DoctorPatient, Document, Food, Medication, Symptom, Testing

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Comment)
admin.site.register(DietSuggestion)
admin.site.register(DietRestriction)
admin.site.register(DoctorPatient)
admin.site.register(Document)
admin.site.register(Food)
admin.site.register(Medication)
admin.site.register(Symptom)
admin.site.register(Testing)


