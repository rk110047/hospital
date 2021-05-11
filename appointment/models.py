from django.db import models
from authentication.models import SubUser
from vaccine.models import Vaccine,VaccineGroups
from django.contrib.auth import get_user_model
from .utils import unique_id_generator
from django.db.models.signals import pre_save
# Create your models here.


User 	=	get_user_model()


class Appointment(models.Model):
	appointment_id		=		models.CharField(max_length=120)
	user 				=		models.ForeignKey(User,on_delete=models.CASCADE)
	patient  			=		models.ForeignKey(SubUser,on_delete=models.CASCADE)
	vaccine 			=		models.ForeignKey(Vaccine,on_delete=models.CASCADE,null=True,blank=True)
	vaccine_group 		=		models.ForeignKey(VaccineGroups,on_delete=models.CASCADE,null=True,blank=True)
	appoitment_date 	=		models.DateField()
	

	def __str__(self):
		return F'{self.patient}'


def pre_save_appointment_id_creator(instance,sender,*args,**kwargs):
    if not instance.appointment_id:
        instance.appointment_id = unique_id_generator(instance)


pre_save.connect(pre_save_appointment_id_creator,sender=Appointment)


