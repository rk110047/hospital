from django.urls import path
from .views import HospitalListAPIView

urlpatterns=[
	path('list/',HospitalListAPIView.as_view(),name='hospital-list')
	]
