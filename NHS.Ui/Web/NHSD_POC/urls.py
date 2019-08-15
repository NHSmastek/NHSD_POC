from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('PatientPathwayTimeline', views.PatientPathwayTimeline, name='PatientPathwayTimeline'),
]