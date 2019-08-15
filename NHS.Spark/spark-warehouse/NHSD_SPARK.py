import findspark
import riak_machine

findspark.init()
from pyspark import SparkContext
from pyspark.sql import *
from pyspark.sql.functions import col
# conf = SparkConf().setAppName("appName").setMaster("local") 
# sc = spark.sparkContext.getOrCreate(conf=conf)
sc = SparkContext("local", "Simple App").getOrCreate()
spark = SparkSession(sc)
path = "D:\PTL_50k.csv"
df = spark.read.csv(path,inferSchema=True,header=True)
# df.printSchema()
# df.show(50000)

df.createOrReplaceTempView("recordView")
sqlDF = spark.sql("SELECT * FROM recordView")
# sqlDF.show()
sqlDF.printSchema()

riak=riak_machine.riak_machine()
trust_data="TrustData   :{RR1:{E1:95,E2:96,E3:97,E4:50}, RR2:{E1:95,E2:96,E3:97,E4:50}, RR3:{E1:95,E2:96,E3:97,E4:50},RR4:{E1:95,E2:96,E3:97,E4:50}}"
region_data="RegionData :{R1:{E1:95,E2:96,E3:97,E4:50},R2:{E1:95,E2:96,E3:97,E4:50},R3:{E1:95,E2:96,E3:97,E4:50},R8:{E1:95,E2:96,E3:97,E4:50} }"



riak.write_to_riak("TrustPerformance","TrustData",trust_data)
riak.write_to_riak("RegionPerformance","RegionData",region_data)
