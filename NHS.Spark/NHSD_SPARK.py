import findspark
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
sqlDF = spark.sql("SELECT * FROM recordView  ")
# sqlDF.show()
sqlDF.printSchema()
