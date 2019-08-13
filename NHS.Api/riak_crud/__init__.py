import riak


def create_client():
    client = riak.RiakClient(host="3.16.26.40")
    return client


riak_client = create_client()
trust_bucket_name = "trust_performance"
region_bucket_name = "region_performance"
