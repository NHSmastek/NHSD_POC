
import findspark
findspark.init()
from riak_connector import Riak_Connector as rc
from pyspark.sql.functions import col, datediff, unix_timestamp
from analyticConfigs import config, sparkReadFormat
import json
import os
from datetime import date, datetime
from pyspark.sql import *
from pyspark import SparkContext



class Analytics(object):

    def run_Analytic_Engine(self):
        sc = SparkContext(str(config['App_Path']),str( config['App_Name'])).getOrCreate()
        spark=SparkSession(sc)
        trustFilePath=''
        pathMappingFilePath=''
        if config['IsLocal']:
            trustFilePath=os.path.join(os.getcwd(), '..\\Csvs\\'+config['Files']['TrustDataFile'])
            pathMappingFilePath=os.path.join(os.getcwd(), '..\\Csvs\\'+config['Files']['TrustRegionMappingFile'])
        else:
            trustFilePath=config['Files']['TrustDataFile']
            pathMappingFilePath=config['Files']['TrustRegionMappingFile']

        df=spark.read.format("com.databricks.spark.csv")\
            .option("header",str( sparkReadFormat['options']['header']))\
                .option("treatEmptyValuesAsNulls", str( sparkReadFormat['options']['treatEmptyValuesAsNulls']))\
                    .option("inferSchema", str( sparkReadFormat['options']['inferSchema']))\
                        .option("mode",str( sparkReadFormat['options']['mode']))\
                            .option("timestampFormat", str( sparkReadFormat['options']['timestampFormat']))\
                                .load(trustFilePath)

        dfMapping=spark.read.format("com.databricks.spark.csv")\
            .option("header",str( sparkReadFormat['options']['header']))\
                .option("treatEmptyValuesAsNulls", str( sparkReadFormat['options']['treatEmptyValuesAsNulls']))\
                    .option("inferSchema", str( sparkReadFormat['options']['inferSchema']))\
                        .option("mode",str( sparkReadFormat['options']['mode']))\
                            .load(pathMappingFilePath)

        df.show()
        dfMapping.printSchema()
        dfMapping.show()
        df.printSchema()

        df_final=df.alias('df1').join(df.alias('df2'), 'Nhs_No', 'inner').join(df.alias('df3'), 'Nhs_No', 'inner').join(df.alias(
            'df4'), 'Nhs_No', 'inner').join(df.alias('df5'), 'Nhs_No', 'inner').join(dfMapping.alias('dfMapping'), 'Org_Code', 'inner')\
            .where('df1.Event_Id == "E1"')\
                .where('df2.Event_Id == "E2"').where('df3.Event_Id == "E3"').where('df4.Event_Id == "E4"').where('df5.Event_Id == "E5"')\
                    .select(col('df1.Event_Id'), col('df1.Nhs_No'), col('df1.Org_Code'), col('dfMapping.region_id'), datediff('df2.Date', 'df1.Date').alias('E1_days'), datediff('df3.Date', 'df2.Date').alias('E2_days'),\
                            datediff('df4.Date', 'df3.Date').alias('E3_days'), datediff('df5.Date', 'df4.Date').alias('E4_days'))\


        df_final.printSchema()
        df_final.show()
        print("**********************************************************************************************")
        print("The org performance data")
        df_trust_performance=df_final.groupBy(df_final.Org_Code).agg(
            {"E1_days": "avg", "E2_days": "avg", "E3_days": "avg", "E4_days": "avg"})\
            .select(col("Org_Code"), col("avg(E1_days)").alias("E1"), col("avg(E2_days)").alias("E2"), col("avg(E3_days)").alias("E3"), col("avg(E4_days)").alias("E4"))

        df_Region_performance=df_final.groupBy(df_final.region_id).agg(
            {"E1_days": "avg", "E2_days": "avg", "E3_days": "avg", "E4_days": "avg"})\
            .select(col("region_id"), col("avg(E1_days)").alias("E1"), col("avg(E2_days)").alias("E2"), col("avg(E3_days)").alias("E3"), col("avg(E4_days)").alias("E4"))


        trust_data=df_trust_performance.toJSON().map(lambda j: json.loads(j)).collect()
        region_data=df_Region_performance.toJSON().map(lambda j: json.loads(j)).collect()

        # print(trust_data)


        # print("**********************************************************************************************","The region performance data",region_data)
        # trust_data="TrustData:{RR1:{E1:95,E2:96,E3:97,E4:50}, RR2:{E1:95,E2:96,E3:97,E4:50}, RR3:{E1:95,E2:96,E3:97,E4:50},RR4:{E1:95,E2:96,E3:97,E4:50}}"
        # region_data="RegionData:{R1:{E1:95,E2:96,E3:97,E4:50},R2:{E1:95,E2:96,E3:97,E4:50},R3:{E1:95,E2:96,E3:97,E4:50},R8:{E1:95,E2:96,E3:97,E4:50} }"

        rc.getRc().write_to_riak(config['Riak']['Buckets']['Trust'], config['Riak']['BucketsKey']['Trust'], trust_data)
        rc.getRc().write_to_riak(config['Riak']['Buckets']['Region'], config['Riak']['BucketsKey']['Region'], trust_data)
