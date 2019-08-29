from django.http import JsonResponse, HttpResponse
import NHS_AnalyticsAPI
from .AnalyticConfig import config
from .riak_connector import Riak_Connector as rc
from django.core.serializers.json import DjangoJSONEncoder
import json
import random


def get_trust_list(request):
    trust_list = []
    regions = rc.getRc().get_keys(config['Riak']['Buckets']['Trusts_Region_Map'])
    for region in regions:
        trust_list.extend(rc.getRc().get_by_key(config['Riak']['Buckets']['Trusts_Region_Map'], region))
    return JsonResponse(trust_list, safe=False)


def search_trust(request, trust_name):
    # Get Region Code
    region_code = _get_region_code_for_trust(trust_name)
    if not region_code:
        return HttpResponse("This Trust Is Not Present In Any of specified Regions")
    # Get Trust Peer List
    peer_list = _get_peer_list(trust_name, region_code)
    if not peer_list:
        return HttpResponse("Not able to get peers for this trust")
    region_dict = _get_region_list()
    if not region_dict:
        return HttpResponse(content="No Region Exists", status=404)
    resp_data = {
        "Region_Code": region_code,
        "Region_Data": region_dict,
        "Trust_Data": peer_list,
    }
    return JsonResponse(resp_data, safe=False)


def _get_peer_list(trust_name, region_code):
    peer_list = {}
    peer_id_list = random.sample(rc.getRc().get_by_key(config['Riak']['Buckets']['Trusts_Region_Map'], region_code), 4)
    if trust_name not in peer_id_list:
        peer_id_list[0] = trust_name
    for item in peer_id_list:
        tempdict = rc.getRc().get_by_inner_key(
            config['Riak']['Buckets']['Trust'], 'Org_Code', item)
        peer_list[list(tempdict.keys())[0]] = list(tempdict.values())[0]
    return peer_list


def _get_region_code_for_trust(trust_name):
    keys = rc.getRc().get_keys(config['Riak']['Buckets']['Trusts_Region_Map'])
    for key in keys:
        rc.getRc().get_by_key(config['Riak']['Buckets']['Trusts_Region_Map'], key)
        if trust_name in rc.getRc().get_by_key(config['Riak']['Buckets']['Trusts_Region_Map'], key):
            return key


def _get_region_list():
    region_dict = {}
    region_obj = rc.getRc().get_by_key(
        config['Riak']['Buckets']['Region'], config['Riak']['BucketsKey']['Region'])
    for region in region_obj:
        region_dict[region["Region_Code"]] = region
    return region_dict
