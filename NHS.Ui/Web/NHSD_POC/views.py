from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required

# def get_trust_list(request, trust_name):
#     #url = "{}:{}/search_trust/{}".format(settings.NHS_API_DOMAIN_NAME, settings.NHS_API_DOMAIN_PORT, trust_name)
#     url = "http://172.16.243.211:8009/getDummy"
#     trust_performance_obj = requests.get(url=url)
#     trust_performance = trust_performance_obj.json()
#     return JsonResponse(trust_performance)

@login_required
def patient_pathway_timeline(request):
    url = "{}:{}/get_trust_list".format(settings.NHS_API_DOMAIN_NAME, settings.NHS_API_DOMAIN_PORT)
    trust_list_obj = requests.get(url=url)
    return render(request, "NHSD_POC/trust_performance.html", {"trust_list": trust_list_obj.json()})
