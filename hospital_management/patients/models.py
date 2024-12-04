from django.db import models

class Patient(models.Model):
    # Patient ID (auto-incremented primary key)
    pid = models.AutoField(primary_key=True)
    
    # Patient's Name
    pname = models.CharField(max_length=200)
    
    # Patient's Gender (you can choose other options like choices if needed)
    gender = models.CharField(max_length=10)
    
    # Patient's Fee (could be a DecimalField to handle monetary values)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Patient's Age
    age = models.IntegerField()
    
    # Ward Name where the patient is placed
    ward = models.CharField(max_length=100)
    
    # Disease Name
    disease = models.CharField(max_length=200)

    def __str__(self):
        return self.pname


# Create your models here.
