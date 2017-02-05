from django.db import models


class Comment(models.Model):
    doctor = models.IntegerField(default=-1)
    patient = models.IntegerField(default=-1)
    comment = models.CharField(default="This comment was blank", max_length=1024)
    date = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=False)


class DietRestriction(models.Model):
    food = models.CharField(default="No name given", max_length=50)
    category = models.CharField(default="Not Categorized", max_length=40)
    patient = models.IntegerField(default=-1)
    doctor = models.IntegerField(default=-1)


class DietSuggestion(models.Model):
    food = models.CharField(default="No name given", max_length=50)
    category = models.CharField(default="Not Categorized", max_length=40)
    servings = models.IntegerField(default=0)
    patient = models.IntegerField(default=-1)
    doctor = models.IntegerField(default=-1)


class Doctor(models.Model):
    prefix = models.CharField(max_length=10, default="Dr.")
    firstname = models.CharField(max_length=25, default="Doctor")
    lastname = models.CharField(max_length=25, default="Nurse")
    email = models.EmailField(default="doctor@placeholder.com")
    phone = models.IntegerField(default="6130000000")
    specialty = models.CharField(max_length=50, default="Proctology")
    photo = models.ImageField(upload_to='media/',
                              null=True, max_length=255)


class DoctorPatient(models.Model):
    doctor = models.IntegerField(default=1)
    patient = models.IntegerField(default=1)


class Document(models.Model):
    doctor = models.IntegerField(default=-1)
    patient = models.IntegerField(default=-1)
    description = models.CharField(default="No description available", max_length=2048)
    file = models.FileField(upload_to='media/',
                            null=True, max_length=255,)
    date = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=False)


class Food(models.Model):
    name = models.CharField(max_length=50, default="Nothing")
    brandName = models.CharField(max_length=50, default="N/A")
    servingQuantity = models.IntegerField(default=1)
    servingUnit = models.CharField(default="None", max_length=50)
    calories = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    totalFats = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    satFats = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    cholesterol = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    sodium = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    carbs = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    sugar = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    protein = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    thumb = models.URLField(default="None available")
    highres = models.URLField(default="None available")
    datetime = models.DateTimeField(auto_now=True)
    patient = models.IntegerField(default=-1)


class Medication(models.Model):
    doctor = models.IntegerField(default=-1)
    patient = models.IntegerField(default=-1)
    medication = models.CharField(default='Tylenol', max_length=255)
    reason = models.CharField(default='No reason available', max_length=1024)
    dose = models.CharField(default='1 a day', max_length=255)
    date = models.DateTimeField(auto_now=True)


class Patient(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, default=1)
    firstname = models.CharField(max_length=25, default="Testy")
    lastname = models.CharField(max_length=25, default="Tester")
    email = models.EmailField(default="tester@placeholder.com")
    password = models.CharField(default="fakepassword", max_length=40)
    phone = models.CharField(default="5191231234", max_length=20)
    age = models.IntegerField(default=-1)
    weight = models.IntegerField(default=-1)
    height = models.IntegerField(default=-1)
    gender = models.CharField(default="Male", max_length=10)
    healthcard = models.IntegerField(default=000000000, primary_key=False)
    status = models.CharField(default="Stable", max_length=25)
    lastseen = models.IntegerField(default=-1)
    reason = models.CharField(default="Knife fights. Yes, plural.", max_length=2048)
    photo = models.ImageField(upload_to='media/',
                              null=True, max_length=255)


class Symptom(models.Model):
    patient = models.IntegerField(default=-1)
    date = models.DateTimeField(auto_now=True)
    symptom = models.CharField(default='Sniffles', max_length=140)


class Testing(models.Model):
    doctor = models.IntegerField(default=-1)
    patient = models.IntegerField(default=-1)
    testname = models.CharField(default='Scan', max_length=130)
    reason = models.CharField(default='No reason given', max_length=2048)
    date = models.DateTimeField(auto_now=True)
