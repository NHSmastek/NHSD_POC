import riak
from django.conf import settings


def create_client():
    client = riak.RiakClient(host=settings.RIAK_HOST_IP, http_port=settings.RIAK_HOST_PORT)
    return client


riak_client = create_client()
