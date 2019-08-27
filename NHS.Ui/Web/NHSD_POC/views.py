from __future__ import unicode_literals
from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from NHSD_POC.AnalyticWebConfigs import config 

@login_required
def patient_pathway_timeline(request):
    url = "{}:{}{}".format(config["Anaytics_API"]["Private_Host"],config["Anaytics_API"]["Port"],config["EndPoints"]["get_trust_list"] )
    trust_list_obj = requests.get(url=url)
    api_url = "{}:{}/".format(config["Anaytics_API"]["Public_Host"],config["Anaytics_API"]["Port"])
    return render(request, config["Template"]["Trust_Performance"], {"trust_list": trust_list_obj.json(),"api_url":api_url})
