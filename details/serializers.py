from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework import serializers


from custom.models import User
from .models import *


class DoctorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['user', 'location']


class SpecialitySerializer(serializers.ModelSerializer):
    number_of_doctors = serializers.IntegerField(read_only=True)
    doctor = DoctorDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Speciality
        fields = ['id', 'name', 'description', 'number_of_doctors', 'doctor']


class UserDetailSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=50)
    confirm_password = serializers.CharField(write_only=True, max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'confirm_password']

class PatientRegistrationSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Patient
        fields = ['id', 'user']
    
    
    def save(self, **kwargs):
        with transaction.atomic():
            user = dict(self.validated_data['user'])
            password = user['password']
            confirm_password = user['confirm_password']

            if password == confirm_password:

                user = User.objects.create_user(username=user['username'], first_name=user['first_name'], last_name=user['last_name'], email=user['email'], password=user['password'])

                patient = Patient.objects.create(user=user)

                return patient
            else:
                raise serializers.ValidationError('Passwords do not match')

class AvailabilityDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = ['date', 'time']

class DoctorRegistrationSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    availability = AvailabilityDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'user', 'location', 'speciality', 'availability']
    
    
    def save(self, **kwargs):
        with transaction.atomic():
            user = dict(self.validated_data['user'])
            password = user['password']
            confirm_password = user['confirm_password']
            location = self.validated_data['location']
            speciality = self.validated_data['speciality']

            if password == confirm_password:

                user = User.objects.create_user(username=user['username'], first_name=user['first_name'], last_name=user['last_name'], email=user['email'], password=user['password'])

                doctor = Doctor.objects.create(user=user, location=location, speciality=speciality)

                return doctor
            else:
                raise serializers.ValidationError('Passwords do not match')

class NurseRegistrationSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Nurse
        fields = ['user', 'location']

    def save(self, **kwargs):
        with transaction.atomic():
            user = dict(self.validated_data['user'])
            password = user['password']
            confirm_password = user['confirm_password']
            location = self.validated_data['location']
            

            if password == confirm_password:

                user = User.objects.create_user(username=user['username'], first_name=user['first_name'], last_name=user['last_name'], email=user['email'], password=user['password'])

                nurse = Nurse.objects.create(user=user, location=location)

                return nurse
            else:
                raise serializers.ValidationError('Passwords do not match')



class PharmacyRegistrationSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Pharmacy
        fields = ['user', 'location']

    def save(self, **kwargs):
        with transaction.atomic():
            user = dict(self.validated_data['user'])
            password = user['password']
            confirm_password = user['confirm_password']
            location = self.validated_data['location']
            

            if password == confirm_password:

                user = User.objects.create_user(username=user['username'], first_name=user['first_name'], last_name=user['last_name'], email=user['email'], password=user['password'])

                pharmacy = Pharmacy.objects.create(user=user, location=location)

                return pharmacy
            else:
                raise serializers.ValidationError('Passwords do not match')



class LabRegistrationSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Lab
        fields = ['user', 'location']

    def save(self, **kwargs):
        with transaction.atomic():
            user = dict(self.validated_data['user'])
            password = user['password']
            confirm_password = user['confirm_password']
            location = self.validated_data['location']
            

            if password == confirm_password:

                user = User.objects.create_user(username=user['username'], first_name=user['first_name'], last_name=user['last_name'], email=user['email'], password=user['password'])

                lab = Lab.objects.create(user=user, location=location)

                return lab
            else:
                raise serializers.ValidationError('Passwords do not match')



class CreateAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = ['date', 'time']


    def save(self, **kwargs):
        doctor_id = self.context['doctor_id']
        date = self.validated_data['date']
        time = self.validated_data['time']

        availability = DoctorAvailability.objects.create(doctor_id=doctor_id, date=date, time=time)

        return availability


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, data):
        user = authenticate(**data)
        
        if user and user.is_active:
            return user
        
        raise serializers.ValidationError('Incorrect credentials')


class PatientConsultation(serializers.ModelSerializer):
    class Meta:
        model = PatientConsultation
        fields = ['doctor']