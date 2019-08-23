import riak

class riak_machine:
    def get_riak_instance(self):
        client = riak.RiakClient(host="18.220.160.111")
        return client

    def write_to_riak(self, bucket_name, key,DATA):
        self.__delete(bucket_name,key)
        bucket = self.get_or_create_bucket(bucket_name)
        trust_data = bucket.new(key, data=DATA)
        trust_data.store()
        print("Write Success")
    
    def get_or_create_bucket(self, bucket_name):
        return self.get_riak_instance().bucket(bucket_name)


    def __delete(self, bucket_name, key):
        bucket = self.get_or_create_bucket(bucket_name)
        bucket.delete(key)
        return True