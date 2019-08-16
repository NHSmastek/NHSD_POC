from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.conf import settings


def patient_pathway_timeline(request):
    url = "{}:{}/search_trust/".format(settings.NHS_API_DOMAIN_NAME, settings.NHS_API_DOMAIN_PORT)
    # The name of trust will come from drop down for time being hard coded the name of trust
    url += "RR8"
    trust_performance_obj = requests.get(url=url)
    trust_performance = trust_performance_obj.json()
    print(trust_performance)
    return HttpResponse("It will get replaced by view.")


def get_trust_list(request):
    return render(request, "NHSD_POC/trust_performance.html", {})
