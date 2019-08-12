import riak


def create_client():
    # client = riak.RiakClient(host="18.217.190.19")
    client = riak.RiakClient(host="18.188.197.228")
    return client


riak_client = create_client()
bucket_name = "trust_performance"
