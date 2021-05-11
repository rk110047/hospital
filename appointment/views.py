from django.shortcuts import render
from rest_framework.response import Response
from .serializer import AppointmentSerializer,AppointmentListSerializer
from .models import Appointment
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from django.contrib.auth import get_user_model
from authentication.models import SubUser
from vaccine.models import Vaccine
# Create your views here.

User=get_user_model()


class AppointMentCreateAPIView(generics.CreateAPIView):
	queryset 			=		Appointment.objects.all()
	serializer_class 	=		AppointmentSerializer
	authentication_classses 		=	[]
	permission_classes    			=	[]


class AppointmentCreateAPIView(generics.GenericAPIView):
	authentication_classses 		=	[]
	permission_classes    			=	[]
	queryset 			=		Appointment.objects.all()
	serializer_class 	=		AppointmentSerializer

	def patch(self,request,*args,**kwargs):
		try:
			appointment_id		=		request.data.get('appointment_id')
			user 				=		request.data['user']
			user 				=		User.objects.get(id=user)
			patient  			=		request.data['patient']
			patient 			=		SubUser.objects.get(id=patient)
			vaccine 			=		request.data['vaccine']
			vaccine 			=		Vaccine.objects.get(id=vaccine)
			appoitment_date 	=		request.data['appoitment_date']
			Appointment.objects.create(appointment_id=appointment_id,user=user,patient=patient,vaccine=vaccine,appoitment_date=appoitment_date)
			return Response({'message':"created",'status':201})
		except:
			return Response({'message':"failed"})


class AppointMentListAPIView(generics.GenericAPIView):
	authentication_classses 		=	[SessionAuthentication,TokenAuthentication]
	permission_classes    			=	[]
	queryset 			=		Appointment.objects.all()
	serializer_class 	=		AppointmentListSerializer

	def get(self,request):
		user 		=		self.request.user
		query 		= 		Appointment.objects.filter(user=user)
		serialize   =		AppointmentListSerializer(query,many=True,context={'request': request})
		return Response(serialize.data)

class AppointMentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
        authentication_classses                 =       [SessionAuthentication,TokenAuthentication]
        permission_classes                      =       []
        queryset                        =               Appointment.objects.all()
        serializer_class        =               AppointmentListSerializer
        lookup_field 			=		"id"



