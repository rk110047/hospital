from django.urls import path
from .views import VaccineTypeListCreateAPIVIew,VaccinesOfHospitalsAPIView,VaccineGroupsListCreateAPIVIew


app_name="vaccine"

urlpatterns=[
	path('vaccine-types/',VaccineTypeListCreateAPIVIew.as_view(),name='vaccine-types'),
	path('vaccine-groups/',VaccineGroupsListCreateAPIVIew.as_view(),name='vaccine-groups'),
	path('vaccines/<id>/',VaccinesOfHospitalsAPIView.as_view(),name='vaccines')

]