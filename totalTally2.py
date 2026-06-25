from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

# inialize spark obj
spark = SparkSession.builder.appName('TotalSales').master("local[*]").getOrCreate()

# create schema
schema = StructType([
    StructField('cust_id',IntegerType(),True),
    StructField('item_id',IntegerType(),True),
    StructField('amount_spent',FloatType(),True)
])

# Load data
df = spark.read.schema(schema).csv('customer-orders.csv')

totalByCustomer = df.groupBy("cust_id").agg(func.round(func.sum("amount_spent"), 2).alias("total_spent"))

totalByCustomerSorted = totalByCustomer.sort("total_spent")

totalByCustomerSorted.show(totalByCustomerSorted.count())
# df.show()
spark.stop()