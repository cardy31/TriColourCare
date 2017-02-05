from rest_framework import serializers
from django.contrib.auth.models import User
from server.models import Comment, DietRestriction, DietSuggestion, Doctor, Document, Food, Patient,\
    Medication, DoctorPatient, Symptom, Testing


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('url', 'id', 'doctor', 'patient', 'comment', 'private')


class DietRestrictionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DietRestriction
        fields = ('url', 'id', 'food', 'category', 'patient', 'doctor')


class DietSuggestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DietSuggestion
        fields = ('url', 'id', 'food', 'category', 'servings', 'patient', 'doctor')


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ('url', 'id', 'prefix', 'firstname', 'lastname', 'email', 'password', 'phone', 'specialty', 'photo',)


class DoctorPatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorPatient
        fields = ('url', 'id', 'doctor', 'patient',)


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('url', 'id', 'doctor', 'patient', 'description', 'file', 'date', 'private')


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ('url', 'id', 'name', 'brandName', 'servingQuantity', 'servingUnit', 'calories', 'totalFats', 'satFats',
                  'cholesterol', 'sodium', 'carbs', 'sugar', 'protein', 'datetime', 'thumb', 'highres', 'patient')


class PatientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Patient
        fields = ('url', 'id', 'firstname', 'lastname', 'email', 'password', 'phone', 'age',
                  'weight', 'height', 'gender', 'healthcard', 'status', 'lastseen', 'reason', 'photo',)


class MedicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medication
        fields = ('url', 'id', 'doctor', 'patient', 'medication', 'reason', 'dose', 'date')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', )


class SymptomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Symptom
        fields = ('url', 'id', 'patient', 'date', 'symptom')


class TestingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testing
        fields = ('url', 'id', 'doctor', 'patient', 'testname', 'reason', 'date', 'private')
