from django.shortcuts import render
from .models import Hospital
from rest_framework import generics
from .serializer import HospitalSerializer
# Create your views here.


class HospitalListAPIView(generics.ListAPIView):
	queryset 			=	Hospital.objects.all()
	serializer_class	=	HospitalSerializer 	
