# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
import NHS_AnalyticsAPI
import riak
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
import json

# Repetition of CRUD Logic is to be removed.
# Logic of getting Peers is pending.

TrustRegionMapData= {
        'R1': [{'Region_Code':'R1'},'REM', 'RCF', 'RBS', 'RFF', 'RXL', 'RMC', 'RAE', 'RWY', 'RLN', 'RJR', 'RXP', 'RP5', 'RJN', 'RXR', 'RR7', 'RCD', 'RWA', 'RXN', 'RR8', 'RBQ', 'R0A', 'REP', 'RBT', 'RXF', 'RNL', 'RVW', 'RJL', 'RTF', 'RW6', 'RQ6', 'RM3', 'RCU', 'RHQ', 'RTR', 'RE9', 'RVY', 'RBN', 'RWJ', 'RMP', 'RBV', 'REN', 'RTD', 'RFR', 'RET', 'RTX', 'RWW', 'RBL', 'RRF', 'RCB'],
        'R2': [{'Region_Code':'R2'},'RDD', 'RC1', 'RQ3', 'RJF', 'RGT', 'RFS', 'RDE', 'RTG', 'RWH', 'R1L', 'RLT', 'RR1', 'RGQ', 'RGP', 'RNQ', 'RC9', 'RQ8', 'RD8', 'RM1', 'RGN', 'RNS', 'RX1', 'RGM', 'RXK', 'RK5', 'RXW', 'RJC', 'RAJ', 'RNA', 'RQW', 'RCX', 'RL1', 'RRJ', 'RL4', 'RWD', 'RRK', 'RKB', 'RWE', 'RJE', 'RBK', 'RWG', 'RGR', 'RWP', 'RLQ'],
        'R3': [{'Region_Code':'R3'},'RF4', 'R1H', 'RQM', 'RJ6', 'RVR', 'RP4', 'RJ1', 'RQX', 'RYJ', 'RJZ', 'RAX', 'RJ2', 'RAP', 'RT3', 'RAL', 'RAN', 'RJ7', 'RAS', 'RPY', 'RKE', 'RRV'],
        'R4': [{'Region_Code':'R4'},'RTK', 'RXH', 'RXQ', 'RN7', 'RBD', 'RVV', 'RXC', 'RDU', 'RTE', 'RN3', 'RN5', 'R1F', 'RWF', 'RPA', 'RVJ', 'RBZ', 'RTH', 'RK9', 'RD3', 'RHU', 'RPC', 'RHW', 'REF', 'RH8', 'RA2', 'RD1', 'RNZ', 'RTP', 'RBA', 'RDZ', 'RA9', 'RHM', 'RA7', 'RYR', 'RA3', 'RA4']
    }

def get_trust_list(request):
    trm_bucket = NHS_AnalyticsAPI.riak_client.bucket(settings.TRUST_REGION_MAP_BUCKET)
    return JsonResponse(trm_bucket.get_keys(), safe=False)


def search_trust(request, trust_name):
    # Get Bucket
    trust_bucket = _get_or_create_bucket(settings.TRUST_BUCKET_NAME)
    region_bucket = _get_or_create_bucket(settings.REGION_BUCKET_NAME)
    trm_bucket = _get_or_create_bucket(settings.TRUST_REGION_MAP_BUCKET)

    # Get Region Code
    region_code = _get_region_code(trust_name, trm_bucket)

    if not region_code:
        return HttpResponse("Trust Specified Not In Any of 4 Regions")

    # Get Trust Peer List
    peer_list={}
    peer_id_list=[]
    for i in range(1,5):
        peer_id_list.append(TrustRegionMapData["R1"][i])
    
    # peer_id_list.append(_get_trust(trust_bucket.name, TrustRegionMapData["R1"][i]))

    for item in peer_id_list:
        print( item)
        print( 'item')
    
    if trust_name not in peer_id_list:
        peer_id_list[3]=trust_name
       
    for item in peer_id_list:
        tempdict=_get_trust(trust_bucket.name, item) 
        peer_list[tempdict.keys()[0]]=tempdict.values()[0] 

    region_dict = _get_region(region_bucket)
    if not region_dict:
        return HttpResponse(content="No Region Exists", status=404)

    trust_dict =peer_list


    # Form Resp Dict
    resp_data = {
        "Region_Code": region_code,
        "Region_Data": region_dict,
        "Trust_Data": trust_dict,
    }
    resp_data = json.dumps(resp_data, cls=DjangoJSONEncoder)
    return JsonResponse(resp_data, safe=False, status=200)


def _get_peer_list(region_code, trust_name):
    pass


def _get_region_code(trust_name, trm_bucket):

    for key,value in TrustRegionMapData.items():
        # print(item)
        if  trust_name in value:
            print(value[0]["Region_Code"])
            print(key)
            return key
    # trust_region_object = trm_bucket.get(trust_name)
    # return trust_region_object.data


def _get_trust(bucket_name, trust_name):
    trust_dict = {}

    query = NHS_AnalyticsAPI.riak_client.add(bucket_name)
    query_str = "function(v) {\
        var val = JSON.parse(v.values[0].data);\
        for (var key in val) {\
            if (val[key]['Org_Code']=='" + trust_name + "'){\
                return [val[key]];\
            }\
        }\
    }"
    query.map(query_str)

    try:
        for trust_data in query.run():
            trust_dict[trust_name] = trust_data
    except riak.RiakError:
        return trust_dict
    # TODO :- Get Trust Peers
    return trust_dict


def _get_region(region_bucket):
    region_dict = {}
    region_obj = region_bucket.get(settings.REGION_KEY)
    for region in region_obj.data:
        region_dict[region["Region_Code"]] = region
    return region_dict


# @require_POST
def write_trust(request):
    bucket = _get_or_create_bucket(settings.TRUST_BUCKET_NAME)
    trust_data = bucket.new(settings.TRUST_KEY, data=TrustData)
    trust_data.store()
    return HttpResponse("Trust Write Success")


def delete_trust(request):
    bucket = _get_or_create_bucket(settings.TRUST_BUCKET_NAME)
    bucket.delete(settings.TRUST_KEY)
    return HttpResponse("Trust Delete Success")


# @require_POST
def update_trust(reqeust):
    # TODO Add Update Functionality
    return HttpResponse("Trust Update Success")


# @require_POST
def write_region(request):
    region_bucket = _get_or_create_bucket(settings.REGION_BUCKET_NAME)
    region_data = region_bucket.new(settings.REGION_KEY, data=RegionData)
    region_data.store()
    return HttpResponse("Region Write Success")


def delete_region(request):
    region_bucket = _get_or_create_bucket(settings.REGION_BUCKET_NAME)
    region_bucket.delete(settings.REGION_KEY)
    return HttpResponse("Region Delete Success")


# @require_POST
def update_region(request):
    # TODO Add Update Functionality
    return HttpResponse("Region Update Success")


def _get_or_create_bucket(bucket_name):
    return NHS_AnalyticsAPI.riak_client.bucket(bucket_name)
