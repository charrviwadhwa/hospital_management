from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Patient

# View to list all patients


def home(request):
    return render(request, 'patients/home.html')
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

# View to add a new patient
def create_patient(request):
    if request.method == 'POST':
        pname = request.POST['pname']
        gender = request.POST['gender']
        fee = request.POST['fee']
        age = request.POST['age']
        ward = request.POST['ward']
        disease = request.POST['disease']
        
        patient = Patient.objects.create(pname=pname, gender=gender, fee=fee, age=age, ward=ward, disease=disease)
        return redirect('patient_list')
    
    return render(request, 'patients/create_patient.html')

# View to update a patient's details
def update_patient(request, pid):
    # Fetch the patient using the given id (pid)
    patient = get_object_or_404(Patient, pid=pid)
    
    if request.method == 'POST':
        # If the request is POST, update the patient data
        patient.pname = request.POST.get('pname', patient.pname)
        patient.gender = request.POST.get('gender', patient.gender)
        patient.fee = request.POST.get('fee', patient.fee)
        patient.age = request.POST.get('age', patient.age)
        patient.ward = request.POST.get('ward', patient.ward)
        patient.disease = request.POST.get('disease', patient.disease)
        patient.save()  # Save the updated patient object

        return redirect('patient_list')  # Redirect to the patient list page
    
    return render(request, 'patients/update_patient.html', {'patient': patient})

# View to delete a patient
def delete_patient(request, pid):
    patient = Patient.objects.get(pid=pid)
    patient.delete()
    return redirect('patient_list')
