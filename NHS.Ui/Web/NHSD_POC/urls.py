from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('PatientPathwayTimeline', views.patient_pathway_timeline, name='PatientPathwayTimeline'),
]