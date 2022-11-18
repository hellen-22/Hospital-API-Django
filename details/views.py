from django.shortcuts import render
from django.db.models import Count
from rest_framework import viewsets


from .serializers import *
from .models import *
from custom.models import User

# Create your views here.
class SpecialityViewSet(viewsets.ModelViewSet):
    serializer_class = SpecialitySerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            return Speciality.objects.annotate(number_of_doctors=Count('doctor'))
        return Speciality.objects.all()

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientRegistrationSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorRegistrationSerializer


class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseRegistrationSerializer


class PharmacyViewSet(viewsets.ModelViewSet):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacyRegistrationSerializer


class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = CreateAvailabilitySerializer

    def get_queryset(self):
        return DoctorAvailability.objects.filter(doctor_id=self.kwargs['doctor_pk'])

    def get_serializer_context(self):
        return {'doctor_id': self.kwargs['doctor_pk']}


class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
