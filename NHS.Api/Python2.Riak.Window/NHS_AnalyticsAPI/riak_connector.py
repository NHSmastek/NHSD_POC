from __future__ import unicode_literals
import riak
from django.conf import settings
from AnalyticConfig import config

class Riak_Connector:
    
    client=None
    
    def create_client(self):
        self.client = riak.RiakClient(host=config['Riak']['Ip'], http_port=config['Riak']['Port'])
        return self.client

    def get_or_create_bucket(self, bucket_name):
        return self.create_client().bucket(bucket_name)

    def get_data_by_key(self,bucket_name,key):
        return self.get_or_create_bucket(bucket_name).get(key)
 
    def get_data_by_inner_key(self, bucket_name, key_name,key_value):
        reuslt = {}
        query = self.create_client().add(bucket_name)
        query_str = "function(v) {\
            var val = JSON.parse(v.values[0].data);\
                for (var key in val) {\
                    if (val[key]['"+ key_name+"']=='" + key_value + "'){\
                        return [val[key]];\
                            }\
                                }\
                                    }"
        query.map(query_str)
        try:
            for search_data in query.run():
                reuslt[key_value] = search_data
        except riak.RiakError:
            return reuslt
        return reuslt

