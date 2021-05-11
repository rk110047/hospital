from django.db import models
from hospital.models import Hospital
# Create your models here.



class VaccineType(models.Model):
	name 				=		models.CharField(max_length=120)
	description			=		models.TextField(max_length=100)


	def __str__(self):
		return self.name



class Vaccine(models.Model):
	vaccine_name		=		models.ForeignKey(VaccineType,on_delete=models.CASCADE)
	hospital 			=		models.ForeignKey(Hospital,on_delete=models.CASCADE)
	counts 				=		models.IntegerField(default=0)
	brand 				=		models.CharField(max_length=120)



	def __str__(self):
		return F'{self.vaccine_name}' 

class VaccineGroups(models.Model):
	group_name 			=		models.CharField(max_length=120)
	vaccines 			=		models.ManyToManyField(Vaccine) 
	age_group 			=		models.IntegerField()

	def __str__(self):
		return self.group_name
