from django.urls import path

from . import views

urlpatterns = [
    path('', views.patient_pathway_timeline, name='PatientPathwayTimeline'),
    path('PatientPathwayTimeline', views.patient_pathway_timeline, name='PatientPathwayTimeline'),
]