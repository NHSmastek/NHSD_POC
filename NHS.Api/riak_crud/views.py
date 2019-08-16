# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
import riak_crud
from django.conf import settings

# This Hardcoded data is to be removed.
# Schema of DATA is not final yet, It might change.
# Repetition of CRUD Logic is to be removed.
TrustData = {
    "E1": 20,
    "E2": 100,
    "E3": 25,
    "E4": 32,
}

RegionData = {
    "E1": 20,
    "E2": 30,
    "E3": 40,
    "E4": 50,
}

RegionTrustMap = {
    "R0": ["RR1", "RR2"],
    "R1": ["RR3", "RR4", "RR5"],
    "R2": ["RR6", "RR7"],
    "R3": ["RR8", "RR9", "RR10"],
}


def search_trust(request, trust_key):
    # Get Bucket
    trust_bucket = _get_or_create_bucket(settings.TRUST_BUCKET_NAME)
    region_bucket = _get_or_create_bucket(settings.REGION_BUCKET_NAME)

    # Get Region Code
    region_code = None
    for k, v in RegionTrustMap.iteritems():
        if trust_key in v:
            region_code = k
    if not region_code:
        return HttpResponse("Trust Specified Not In Any of 4 Regions")

    # Get Region Dict
    region_dict = _get_region(region_bucket)
    if not region_dict:
        return HttpResponse(content="No Region Exists", status=404)

    # Get Trust Data
    trust_dict = _get_trust(trust_bucket, trust_key)
    if not trust_dict[trust_key]:
        return HttpResponse(content="Requested Trust Key Does Not Exists", status=404)

    # Form Resp Dict
    resp_data = {
        "RegionCode": region_code,
        "RegionData": region_dict,
        "TrustData": trust_dict,
    }
    return JsonResponse(resp_data, safe=False, status=200)


def _get_trust(trust_bucket, trust_key):
    trust_dict = {}
    trust_obj = trust_bucket.get(trust_key)
    trust_dict[trust_key] = trust_obj.data
    # TODO :- Get Trust Peers
    return trust_dict


def _get_region(region_bucket):
    region_dict = {}
    for region_key in region_bucket.get_keys():
        region_obj = region_bucket.get(region_key)
        region_dict[region_key] = region_obj.data
    return region_dict


# @require_POST
def write_trust(request, trust_key):
    bucket = _get_or_create_bucket(settings.TRUST_BUCKET_NAME)
    trust_data = bucket.new(trust_key, data=TrustData)
    trust_data.store()
    return HttpResponse("Trust Write Success")


def delete_trust(request, trust_key):
    bucket = _get_or_create_bucket(settings.TRUST_BUCKET_NAME)
    bucket.delete(trust_key)
    return HttpResponse("Trust Delete Success")


# @require_POST
def update_trust(reqeust, trust_key):
    # TODO Add Update Functionality
    return HttpResponse("Trust Update Success")


# @require_POST
def write_region(request, region_key):
    region_bucket = _get_or_create_bucket(settings.REGION_BUCKET_NAME)
    region_data = region_bucket.new(region_key, data=RegionData)
    region_data.store()
    return HttpResponse("Region Write Success")


def delete_region(request, region_key):
    region_bucket = _get_or_create_bucket(settings.REGION_BUCKET_NAME)
    region_bucket.delete(region_key)
    return HttpResponse("Region Delete Success")


# @require_POST
def update_region(request, region_key):
    # TODO Add Update Functionality
    return HttpResponse("Region Update Success")


def _get_or_create_bucket(bucket_name):
    return riak_crud.riak_client.bucket(bucket_name)

