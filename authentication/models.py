from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User 		=		get_user_model()

class SubUser(models.Model):
	user 		=		models.ForeignKey(User,on_delete=models.CASCADE)
	name 		=		models.CharField(max_length=120)
	relation 	=		models.CharField(max_length=120)
	age 		=		models.CharField(max_length=120)
	profession  =       models.CharField(max_length=120)
	image           =   models.FileField(upload_to='subprofile/', null=True, verbose_name="")

	def __str__(self):
		return 	self.name
