from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, IntegerType, LongType

# initialize Spark
spark = SparkSession.builder.appName('PopularMovis').getOrCreate()

# define Schema as no header in the csv
schema = StructType([
    StructField("userID",IntegerType(),True),
    StructField("movieID",IntegerType(),True),
    StructField("rating",IntegerType(),True),
    StructField("timestamp",LongType(),True)
])

# load data
moviesDF = spark.read.option("sep","\t").schema(schema).csv("ml-100k/u.data")

# SQL style sort all movie by popularity
topMovieIDs = moviesDF.groupBy("movieID").count().orderBy(func.desc("count"))

# Display top 10 
topMovieIDs.show(10)

spark.stop()
