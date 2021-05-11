from django.urls import path
from .views import AppointMentCreateAPIView,AppointMentListAPIView,AppointmentCreateAPIView,AppointMentRUDAPIView

app_name="appointment"
urlpatterns=[
	path('Create/',AppointmentCreateAPIView.as_view(),name='create'),
	path('create/',AppointMentCreateAPIView.as_view(),name='appointment-create'),
	path('list/',AppointMentListAPIView.as_view(),name='appointment-list'),
        path('rud/<id>/',AppointMentRUDAPIView.as_view(),name='appointment-rud')

]
