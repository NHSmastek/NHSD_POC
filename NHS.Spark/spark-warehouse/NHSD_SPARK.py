import findspark
findspark.init()

from pyspark.sql.functions import col, datediff, unix_timestamp
from datetime import date, datetime
from pyspark.sql import *
from pyspark import SparkContext
import riak_machine
import json

sc = SparkContext("local", "Simple App").getOrCreate()
spark = SparkSession(sc)
trust_File_Path = "D:\python\NHSD_POC\NHS.Spark\Csvs\NhsdSampleData_1Lac.csv"
mapping_File_Path = "D:\python\NHSD_POC\NHS.Spark\Csvs\NhsdROMapping.csv"

df_Trust = spark.read.format("com.databricks.spark.csv")\
    .option("header", "True")\
    .option("treatEmptyValuesAsNulls", "true")\
    .option("inferSchema", "true")\
    .option("mode", "DROPMALFORMED")\
    .option("timestampFormat", "MM-dd-yyyy hh mm ss")\
    .load(trust_File_Path)

df_Trust_Region_Mapping = spark.read.format("com.databricks.spark.csv")\
    .option("header", "True")\
    .option("treatEmptyValuesAsNulls", "true")\
    .option("inferSchema", "true")\
    .option("mode", "DROPMALFORMED")\
    .load(mapping_File_Path)

df_Trust_Region_Mapping.printSchema()
df_Trust.printSchema()

df_Differential = df_Trust.alias('df_E1').join(df_Trust.alias('df_E2'), 'Nhs_No', 'inner').join(df_Trust.alias('df_E3'), 'Nhs_No', 'inner').join(df_Trust.alias('df_E4'), 'Nhs_No', 'inner').join(df_Trust.alias('df_E5'), 'Nhs_No', 'inner').join(df_Trust_Region_Mapping.alias('df_Trust_Region_Mapping'), 'Org_Code', 'inner')\
    .where('df_E1.Event_Id == "E1"')\
    .where('df_E2.Event_Id == "E2"').where('df_E3.Event_Id == "E3"').where('df_E4.Event_Id == "E4"').where('df_E5.Event_Id == "E5"')\
    .select(col('df_E1.Event_Id'), col('df_E1.Nhs_No'), col('df_E1.Org_Code'), col('df_Trust_Region_Mapping.region_id'), datediff('df_E2.Date', 'df_E1.Date').alias('E1_days'), datediff('df_E3.Date', 'df_E2.Date').alias('E2_days'),
            datediff('df_E4.Date', 'df_E3.Date').alias('E3_days'), datediff('df_E5.Date', 'df_E4.Date').alias('E4_days'))

df_Differential.printSchema()
df_Differential.show()


df_Trust_Performance = df_Differential.groupBy(df_Differential.Org_Code).agg({"E1_days": "avg", "E2_days": "avg", "E3_days": "avg", "E4_days": "avg"})\
    .select(col("Org_Code"), col("avg(E1_days)").alias("E1"), col("avg(E2_days)").alias("E2"), col("avg(E3_days)").alias("E3"), col("avg(E4_days)").alias("E4"))

df_Region_Performance = df_Differential.groupBy(df_Differential.region_id).agg({"E1_days": "avg", "E2_days": "avg", "E3_days": "avg", "E4_days": "avg"})\
    .select(col("region_id").alias("Region_Code"), col("avg(E1_days)").alias("E1"), col("avg(E2_days)").alias("E2"), col("avg(E3_days)").alias("E3"), col("avg(E4_days)").alias("E4"))

trust_data = df_Trust_Performance.toJSON().map(lambda j: json.loads(j)).collect()
region_data = df_Region_Performance.toJSON().map(lambda j: json.loads(j)).collect()


riak = riak_machine.riak_machine()

riak.write_to_riak("TrustPerformance","TrustData",trust_data)
riak.write_to_riak("RegionPerformance","RegionData",region_data)
