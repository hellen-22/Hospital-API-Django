from django.db import models

from custom.models import User
# Create your models here.

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
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)

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
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.doctor.user.username
