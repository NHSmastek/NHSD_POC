from django.conf.urls import url, include

urlpatterns = [
    url('', include("NHS_AnalyticsAPI.urls")),
]
