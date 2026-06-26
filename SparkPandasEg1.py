from pyspark.sql import SparkSession
import pandas as pd
import pyspark.pandas as ps
import os
os.environ['PYARROW_IGNORE_TIMEZONE'] = '1'

# Initialize Spark
spark = SparkSession.builder.appName('SparkPanda')\
    .config('spark.sql.ansi.enable','false')\
    .config("spark.executorEnv.PYARROW_IGNORE_TIMEZONE", "1")\
    .getOrCreate()

# create panda df
pandas_df = pd.DataFrame({
    'id': [1,2,3,4],
    'name': ["alpha","bravo","charlie","delta"],
    'age': [24,25,30,23]
})
# print(pandas_df)

# Converting Pandas DF to spark df
spark_df = spark.createDataFrame(pandas_df)

# #schema of spark df
# spark_df.printSchema()

# spark_df.show()

# Applying transformations to spark df
filteredSpark_df = spark_df.filter(spark_df.age > 24)
# filteredSpark_df.show()

# convert spark df to pandas again
converted_df = filteredSpark_df.toPandas()
print(converted_df)



# Using Pandas on Spark dataframe
ps_df = ps.DataFrame(pandas_df)

# Performing Pandas like operations on Pandas on spark df
print('\nIncrementing the age by 1')
ps_df['age'] = ps_df['age']+1
print(ps_df)

# converting pandas on spark df to normal spark df (helpful for cluster)
converted_spark_df = ps_df.to_spark()
converted_spark_df.printSchema()
converted_spark_df.show()

spark.stop()