from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/create/', views.create_patient, name='create_patient'),
    path('patients/update/<int:pid>/', views.update_patient, name='update_patient'),
    path('patients/delete/<int:pid>/', views.delete_patient, name='delete_patient'),
]
