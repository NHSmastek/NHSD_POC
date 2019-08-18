from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
import requests
from django.conf import settings


def get_trust_list(request, trust_name):
    url = "{}:{}/search_trust/{}".format(settings.NHS_API_DOMAIN_NAME, settings.NHS_API_DOMAIN_PORT, trust_name)
    # The name of trust will come from drop down for time being hard coded the name of trust
    trust_performance_obj = requests.get(url=url)
    trust_performance = trust_performance_obj.json()
    return JsonResponse(trust_performance)


def patient_pathway_timeline(request):
    return render(request, "NHSD_POC/trust_performance.html", {})