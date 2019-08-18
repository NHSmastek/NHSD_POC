import findspark
import riak_machine

findspark.init()
from pyspark import SparkContext
from pyspark.sql import *
from pyspark.sql.functions import col,datediff,unix_timestamp
from datetime import date, datetime

sc = SparkContext("local", "Simple App").getOrCreate()
spark = SparkSession(sc)
path = "D:\PTL_50k.csv"
# df = spark.read.csv(path,inferSchema=True,header=True)

df = spark.read.format("com.databricks.spark.csv")\
    .option("header", "True")\
        .option("treatEmptyValuesAsNulls", "true")\
            .option("inferSchema", "true")\
                .option("mode","DROPMALFORMED")\
                    .option("timestampFormat", "MM-dd-yyyy hh mm ss")\
                        .load(path)

df.printSchema()

df_final=df.alias('df1').join(df.alias('df2'), 'Nhs_No' , 'inner').join(df.alias('df3'), 'Nhs_No' , 'inner').join(df.alias('df4'), 'Nhs_No' , 'inner').join(df.alias('df5'), 'Nhs_No' , 'inner')\
    .where('df1.Event_Id == "E1"')\
        .where('df2.Event_Id == "E2"').where('df3.Event_Id == "E3"').where('df4.Event_Id == "E4"').where('df5.Event_Id == "E5"')\
            .select(col('df1.Event_Id'),col('df1.Nhs_No'),col('df1.Org_Code'),col('df1.region_id')\
                ,datediff('df2.Date', 'df1.Date').alias('E1_days'),datediff('df3.Date', 'df2.Date').alias('E2_days'),\
                    datediff('df4.Date', 'df3.Date').alias('E3_days'),datediff('df5.Date', 'df4.Date').alias('E4_days'))

# df.createOrReplaceTempView("recordView")
# sqlDF = spark.sql("SELECT * FROM recordView")
# sqlDF.show()
# sqlDF.printSchema()
df_final.printSchema()
df_final.show()  

df_trust_performance=df_final.groupBy(df_final.Org_Code).agg({"E1_days": "avg","E2_days": "avg","E3_days": "avg","E4_days": "avg"})\
    .select(col("Org_Code"),col("avg(E1_days)").alias("E1_days"),col("avg(E2_days)").alias("E2_days"),col("avg(E3_days)").alias("E3_days"),col("avg(E4_days)").alias("E4_days"))

df_Region_performance=df_final.groupBy(df_final.region_id).agg({"E1_days": "avg","E2_days": "avg","E3_days": "avg","E4_days": "avg"})\
    .select(col("region_id"),col("avg(E1_days)").alias("E1_days"),col("avg(E2_days)").alias("E2_days"),col("avg(E3_days)").alias("E3_days"),col("avg(E4_days)").alias("E4_days"))


trust_data=df_trust_performance.toJSON().collect()
region_data=df_Region_performance.toJSON().collect()

print(trust_data)
print(region_data)
riak=riak_machine.riak_machine()
# trust_data="TrustData   :{RR1:{E1:95,E2:96,E3:97,E4:50}, RR2:{E1:95,E2:96,E3:97,E4:50}, RR3:{E1:95,E2:96,E3:97,E4:50},RR4:{E1:95,E2:96,E3:97,E4:50}}"
# region_data="RegionData :{R1:{E1:95,E2:96,E3:97,E4:50},R2:{E1:95,E2:96,E3:97,E4:50},R3:{E1:95,E2:96,E3:97,E4:50},R8:{E1:95,E2:96,E3:97,E4:50} }"



riak.write_to_riak("TrustPerformance","TrustData",trust_data)
riak.write_to_riak("RegionPerformance","RegionData",region_data)
