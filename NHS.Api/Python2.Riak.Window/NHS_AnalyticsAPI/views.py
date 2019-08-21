# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
import NHS_AnalyticsAPI
import riak
from django.conf import settings

# Repetition of CRUD Logic is to be removed.
# Logic of getting Peers is pending.


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
    peer_list = _get_peer_list(region_code, trust_name)

    # Get Region Dict
    region_dict = _get_region(region_bucket)
    if not region_dict:
        return HttpResponse(content="No Region Exists", status=404)

    # Get Trust Data
    trust_dict = _get_trust(trust_bucket.name, trust_name)
    if not trust_dict[trust_name]:
        return HttpResponse(content="Requested Trust Key Does Not Exists", status=404)

    # Form Resp Dict
    resp_data = {
        "Region_Code": region_code,
        "Region_Data": region_dict,
        "Trust_Data": trust_dict,
    }
    return JsonResponse(resp_data, status=200)


def _get_peer_list(region_code, trust_name):
    pass


def _get_region_code(trust_name, trm_bucket):
    trust_region_object = trm_bucket.get(trust_name)
    return trust_region_object.data


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
