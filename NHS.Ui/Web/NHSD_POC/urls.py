from django.urls import path

from . import views as nhsd_poc

urlpatterns = [
    path('PatientPathwayTimeline', nhsd_poc.patient_pathway_timeline, name='PatientPathwayTimeline'),
    path('<str:trust_name>', nhsd_poc.get_trust_list, name='TrustList'),
]