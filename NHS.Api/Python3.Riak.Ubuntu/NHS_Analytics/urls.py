from django.urls import path, include

urlpatterns = [
    path('', include("NHS_AnalyticsAPI.urls")),
]
