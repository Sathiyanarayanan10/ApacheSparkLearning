from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

spark = SparkSession.builder.appName('MinTemps').getOrCreate()

# Create a schema 
schema = StructType([
    StructField("stationID", StringType(), True),
    StructField("date",IntegerType(),True),
    StructField("measure_type",StringType(),True),
    StructField("temperature",FloatType(),True)
])

# Read the file as DataFrame
df = spark.read.schema(schema).csv("1800.csv")
# df.printSchema()

# Filter out all but TMIN entries
minTemp = df.filter(df.measure_type == 'TMIN')

# Select only the StationID and Temperature
stationTemp = minTemp.select('stationID','temperature')

# aggregate to find minimum temperature for every station
minTempByStation = stationTemp.groupBy('stationID').min('temperature')
# minTempByStation.show()

# Convert this to farenheit 

minTempByStationF = minTempByStation.withColumn('temperature',func.round(
    func.col("min(temperature)") * 0.1 * (9.0/5.0) + 32,2)).select("stationID","temperature").sort('temperature')

results = minTempByStationF.collect()

# Display table
for result in results:
    print(result[0] + "\t{:.2f}F".format(result[1]))

spark.stop()