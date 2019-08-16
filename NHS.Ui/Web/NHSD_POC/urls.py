from django.urls import path

from . import views as nhsd_poc

urlpatterns = [
    path('', nhsd_poc.get_trust_list, name='TrustList'),
    path('PatientPathwayTimeline', nhsd_poc.patient_pathway_timeline, name='PatientPathwayTimeline'),
]