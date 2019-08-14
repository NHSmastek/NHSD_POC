import riak
from django.conf import settings


def create_client():
    # We can specify http port as well. For Now we are using default port.
    client = riak.RiakClient(host=settings.RIAK_HOST_IP)
    return client


riak_client = create_client()
trust_bucket_name = "trust_performance"
region_bucket_name = "region_performance"
