from django.db import models

from custom.models import User

STATUS_CHOICES = (
    ('Complete', 'Complete'),
    ('In Progress', 'In Progress'),
    ('Pending', 'Pending')
)

class Speciality(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='doctor')
    charge = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    bio = models.TextField(null=True)
    certificate = models.FileField(null=True)
    profile_image = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.user.username

class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username

class Pharmacy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username


class Lab(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username

class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availability')
    time = models.TimeField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.doctor.user.username

class PatientConsultation(models.Model):
    availability = models.ForeignKey(DoctorAvailability, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    duration = models.CharField(max_length=255, default=None)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    

    def __str__(self) -> str:
        return f'{self.patient.user.username} Consulting for {self.doctor.speciality}'

