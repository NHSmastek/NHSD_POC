import findspark
import riak_machine
import json
findspark.init()
from pyspark import SparkContext
from pyspark.sql import *
from pyspark.sql.functions import col,datediff,unix_timestamp
from datetime import date, datetime

sc = SparkContext("local", "Simple App").getOrCreate()
spark = SparkSession(sc)
# trustFilePath = "D:\python\NHSD_POC\NHS.Spark\Csvs\NhsdSampleData_50K.csv"
trustFilePath = "D:\python\NHSD_POC\NHS.Spark\Csvs\NhsdSampleData_1Lac.csv"
pathMappingFilePath="D:\python\NHSD_POC\NHS.Spark\Csvs\NhsdROMapping.csv"
# df = spark.read.csv(path,inferSchema=True,header=True)

df = spark.read.format("com.databricks.spark.csv")\
    .option("header", "True")\
        .option("treatEmptyValuesAsNulls", "true")\
            .option("inferSchema", "true")\
                .option("mode","DROPMALFORMED")\
                    .option("timestampFormat", "MM-dd-yyyy hh mm ss")\
                        .load(trustFilePath)

dfMapping = spark.read.format("com.databricks.spark.csv")\
    .option("header", "True")\
        .option("treatEmptyValuesAsNulls", "true")\
            .option("inferSchema", "true")\
                .option("mode","DROPMALFORMED")\
                        .load(pathMappingFilePath)
df.show()
dfMapping.printSchema()
dfMapping.show()
df.printSchema()

df_final=df.alias('df1').join(df.alias('df2'), 'Nhs_No' , 'inner').join(df.alias('df3'), 'Nhs_No' , 'inner').join(df.alias('df4'), 'Nhs_No' , 'inner').join(df.alias('df5'), 'Nhs_No' , 'inner').join(dfMapping.alias('dfMapping'), 'Org_Code' , 'inner')\
    .where('df1.Event_Id == "E1"')\
        .where('df2.Event_Id == "E2"').where('df3.Event_Id == "E3"').where('df4.Event_Id == "E4"').where('df5.Event_Id == "E5"')\
            .select(col('df1.Event_Id'),col('df1.Nhs_No'),col('df1.Org_Code'),col('dfMapping.region_id')\
                ,datediff('df2.Date', 'df1.Date').alias('E1_days'),datediff('df3.Date', 'df2.Date').alias('E2_days'),\
                    datediff('df4.Date', 'df3.Date').alias('E3_days'),datediff('df5.Date', 'df4.Date').alias('E4_days'))

# df.createOrReplaceTempView("recordView")
# sqlDF = spark.sql("SELECT * FROM recordView")
# sqlDF.show()
# sqlDF.printSchema()
df_final.printSchema()
df_final.show()  
print("**********************************************************************************************")
print("The org performance data")
df_trust_performance=df_final.groupBy(df_final.Org_Code).agg({"E1_days": "avg","E2_days": "avg","E3_days": "avg","E4_days": "avg"})\
    .select(col("Org_Code"),col("avg(E1_days)").alias("E1"),col("avg(E2_days)").alias("E2"),col("avg(E3_days)").alias("E3"),col("avg(E4_days)").alias("E4"))

df_Region_performance=df_final.groupBy(df_final.region_id).agg({"E1_days": "avg","E2_days": "avg","E3_days": "avg","E4_days": "avg"})\
    .select(col("region_id"),col("avg(E1_days)").alias("E1"),col("avg(E2_days)").alias("E2"),col("avg(E3_days)").alias("E3"),col("avg(E4_days)").alias("E4"))

# Regionlist=[]
# def f(people):
#     Regiondict={}
#     Regionsubdict={}
#     Regionsubdict["E1"]=people['E1']
#     Regionsubdict["E2"]=people['E2']
#     Regionsubdict["E3"]=people['E3']
#     Regionsubdict["E4"]=people['E4']
#     Regiondict[people['region_id']]=Regionsubdict

#     # print(Regiondict)
#     Regionlist.append(Regiondict)
#     print(Regionlist)
#     # for person in people:
#     #     print(person)


# Trustlist=[]
# def fortrust(people):
#     trustdict={}
#     trustsubdict={}
   
#     trustsubdict["E1"]=people['E1']
#     trustsubdict["E2"]=people['E2']
#     trustsubdict["E3"]=people['E3']
#     trustsubdict["E4"]=people['E4']
#     trustdict["Org_Code"]=people['Org_Code']
#     trustdict["data"]={}
#     trustdict["data"]=trustsubdict
#     # trustdict["Org_Code"]=people['Org_Code']
#     # print(Regiondict)
#     Trustlist.append(Regiondict)
#     print(Trustlist)
#     # for person in people:
#     #     print(person)


trust_data = df_trust_performance.toJSON().map(lambda j: json.loads(j)).collect()
region_data = df_Region_performance.toJSON().map(lambda j: json.loads(j)).collect()
# region_data = df_Region_performance.toJSON().map(lambda j: json.loads({'Region_code':j[0],'data':[{'E1':j[1]}]})).collect()

# print(region_data)
print(trust_data)

# df_Region_performance.foreach(f)
# print(Regionlist)
# trust_data=df_trust_performance.toJSON().collect()
# region_data=df_Region_performance.toJSON().collect()

# df_trust_performance.foreach(fortrust)

# for item in trust_data:
#     print(item)

# print(Regionlist)

# df_Region_performance.groupBy(lambda r: r.region_id).map(
#   lambda g: {
#     'region_id': g[0], 
#     'data': [{'E1': x['E1'], 'E2': x['E2']} for x in g[1]]}
# ).show()

# print(trust_data)
print("**********************************************************************************************","The region performance data",region_data)
riak=riak_machine.riak_machine()
# trust_data="TrustData:{RR1:{E1:95,E2:96,E3:97,E4:50}, RR2:{E1:95,E2:96,E3:97,E4:50}, RR3:{E1:95,E2:96,E3:97,E4:50},RR4:{E1:95,E2:96,E3:97,E4:50}}"
# region_data="RegionData:{R1:{E1:95,E2:96,E3:97,E4:50},R2:{E1:95,E2:96,E3:97,E4:50},R3:{E1:95,E2:96,E3:97,E4:50},R8:{E1:95,E2:96,E3:97,E4:50} }"

# riak.write_to_riak("TrustPerformance","TrustData",trust_data)
# riak.write_to_riak("RegionPerformance","RegionData",region_data)