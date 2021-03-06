import riak
from .AnalyticConfig import config


class Riak_Connector(object):
    __rc = None

    def __init__(self):
        if Riak_Connector.__rc:
            raise Exception("This class is a singleton!")
        else:
            self._client = riak.RiakClient(host=config['Riak']['Ip'], http_port=config['Riak']['Port'])
            Riak_Connector.__rc = self

    @staticmethod
    def getRc():
        if not Riak_Connector.__rc:
            Riak_Connector()
        return Riak_Connector.__rc

    def _bucket(self, bucket_name):
        return self._client.bucket(bucket_name)

    def get_by_key(self, bucket_name, key):
        return self._bucket(bucket_name).get(key).data

    def get_keys(self, bucket_name):
        return self._bucket(bucket_name).get_keys()

    def get_by_inner_key(self, bucket_name, key_name, key_value):
        result = {}
        query = self._client.add(bucket_name)
        query_str = "function(v) {\
            var val = JSON.parse(v.values[0].data);\
                for (var key in val) {\
                    if (val[key]['" + key_name+"']=='" + key_value + "'){\
                        return [val[key]];\
                    }\
                }\
            }"
        query.map(query_str)
        try:
            for search_data in query.run():
                result[key_value] = search_data
        except riak.RiakError:
            return result
        return result
