from django.db import transaction
from rest_framework import serializers


from custom.models import User
from .models import *



class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'name', 'description']


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

class DoctorRegistrationSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Doctor
        fields = ['id', 'user', 'location', 'speciality']
    
    
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



