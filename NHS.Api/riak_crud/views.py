# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
import riak_crud

# This Hardcoded data is to be removed.
# Schema of DATA is not final yet, It might change.
# DATA = {
#    "E1": {
#        "avg_gap": 10,
#        "patient_count": 100,
#    },
#    "E2": {
#        "avg_gap": 5,
#        "patient_count": 100,
#    },
#    "E3": {
#        "avg_gap": 8,
#        "patient_count": 100,
#    },
#    "E4": {
#        "avg_gap": 8,
#        "patient_count": 100,
#    },
#    "E5": {
#        "avg_gap": 6,
#        "patient_count": 100,
#    }
# }

DATA = {
    "E1": 20,
    "E2": 100,
    "E3": 25,
    "E4": 32,
    "E5": 56,
}


def search(request, bucket, key):
    bucket = riak_crud.riak_client.bucket(bucket)
    user_obj = bucket.get(key)
    if not user_obj.data:
        return HttpResponse("No Data with this key is present in this bucket")
    return JsonResponse(user_obj.data)


def write(request, bucket, key):
    bucket = riak_crud.riak_client.bucket(bucket)
    trust_data = bucket.new(key, data=DATA)
    trust_data.store()
    return HttpResponse("Write Success")


def delete(request, bucket, key):
    bucket = riak_crud.riak_client.bucket(bucket)
    bucket.delete(key)
    return HttpResponse("Delete Success")


def update(reqeust, bucket, key):
    return HttpResponse("Update Success")
