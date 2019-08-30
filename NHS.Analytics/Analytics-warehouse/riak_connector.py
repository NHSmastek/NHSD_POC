import riak
from analyticConfigs import config

class Riak_Connector:
    __rc=None
 
    def __init__(self):
       
        if Riak_Connector.__rc!=None:
            raise Exception("This class is a singleton!")
        else:
            self._client = riak.RiakClient(host=config['Riak']['Ip'])
            Riak_Connector.__rc=self

    @staticmethod
    def getRc():
        if Riak_Connector.__rc==None:
            Riak_Connector()
        return Riak_Connector.__rc

    def _bucket(self, bucket_name):
        return self._client.bucket(bucket_name)

    def __delete(self, bucket_name, key):
        bucket = self._bucket(bucket_name)
        bucket.delete(key)
        return True

    def write_to_riak(self, bucket_name, key,DATA):
        self.__delete(bucket_name,key)
        bucket = self._bucket(bucket_name)
        trust_data = bucket.new(key, data=DATA)
        trust_data.store()
        print("Write Success for key {} into bucket {}".format(key,bucket_name))