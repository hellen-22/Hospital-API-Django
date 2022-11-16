from rest_framework_nested import routers
from .views import *
from . import views

router = routers.DefaultRouter()
router.register('speciality', views.SpecialityViewSet, basename='speciality')
router.register('patient', views.PatientViewSet, basename='patient')
router.register('doctor', views.DoctorViewSet, basename='doctor')
router.register('nurse', views.NurseViewSet, basename='nurse')
router.register('pharmacy', views.PharmacyViewSet, basename='pharmacy')



urlpatterns = router.urls