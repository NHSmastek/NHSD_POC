import csv
import riak

RegionTrustMapBucket = "TrustRegionMap"
RTM_File = "NhsdROMapping.csv"


def upload_csv():
    riak_client = riak.RiakClient(host="35.176.37.177", http_port=8087)
    rtm_bucket = riak_client.bucket(RegionTrustMapBucket)
    count = 0
    with open(RTM_File, 'rt') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print("{} ------ {}".format(row["Org_Code"], row["Region_Id"]))
            data = rtm_bucket.new(row['Org_Code'], data=row['Region_Id'])
            data.store()
            count += 1
    print (count)
    riak_client.close()


if __name__ == "__main__":
    upload_csv()