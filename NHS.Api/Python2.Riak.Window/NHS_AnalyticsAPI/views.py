# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
import NHS_AnalyticsAPI
from AnalyticConfig import config
import riak_connector

def get_trust_list(request):
    trm_bucket = riak_connector.Riak_Connector().get_or_create_bucket(
        config['Riak']['Buckets']['TRUST_REGION_MAP'])
    return JsonResponse(trm_bucket.get_keys(), safe=False)

def search_trust(request, trust_name):

    # Get Region Code
    region_code = _get_region_code_for_trust(trust_name)

    if not region_code:
        return HttpResponse("This Trust Is Not Present In Any of specified Regions")

    # Get Trust Peer List
    peer_list = _get_peer_list(trust_name)
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
    return JsonResponse(resp_data, status=200)

def _get_peer_list(trust_name):
    peer_list = {}
    peer_id_list = []
    for i in range(1, 5):
        peer_id_list.append(config['Helper']['TrustRegionMapData']["R1"][i])

    if trust_name not in peer_id_list:
        peer_id_list[3] = trust_name

    for item in peer_id_list:
        tempdict = riak_connector.Riak_Connector().get_data_by_inner_key(
            config['Riak']['Buckets']['Trust'], 'Org_Code', item)
        peer_list[tempdict.keys()[0]] = tempdict.values()[0]
    return peer_list

def _get_region_code_for_trust(trust_name):
    for key, value in config['Helper']['TrustRegionMapData'].items():
        if trust_name in value:
            return key

def _get_region_list():
    region_dict = {}
    region_obj = riak_connector.Riak_Connector().get_data_by_key(
        config['Riak']['Buckets']['Region'], config['Riak']['BucketsKey']['Region'])
    for region in region_obj.data:
        region_dict[region["Region_Code"]] = region
    return region_dict
