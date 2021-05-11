from rest_framework import serializers
from .models import VaccineType,Vaccine,VaccineGroups
from hospital.serializer import HospitalSerializer


class VaccineTypeSerializer(serializers.ModelSerializer):
	vaccines  		=		serializers.HyperlinkedIdentityField(view_name="vaccine:vaccines",lookup_field="id")
	class Meta:
		model 	=	VaccineType
		fields 	=	"__all__"



class VaccineSerializer(serializers.ModelSerializer):
	vaccine_name    =		VaccineTypeSerializer()
	hospital 		=		HospitalSerializer()
	class Meta:
		model 	=	Vaccine
		fields 	=	"__all__"


class VaccineGroupsSerializer(serializers.ModelSerializer):
	vaccines 	=	VaccineSerializer(many=True)	
	class Meta:
		model 	=	VaccineGroups
		fields	=	'__all__'
