from pyspark.sql import SparkSession
# Must set this env variable to avoid warnings
import os
os.environ['PYARROW_IGNORE_TIMEZONE'] = '1'
import pyspark.pandas as ps  # Import pandas-on-Spark

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Pandas API on Spark") \
    .config("spark.sql.ansi.enabled", "false") \
    .config("spark.executorEnv.PYARROW_IGNORE_TIMEZONE", "1") \
    .getOrCreate()

# 1. Create a pandas-on-Spark DataFrame
ps_df = ps.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "age": [25, 30, 35, 40, 45],
    "salary": [50000, 60000, 75000, 80000, 120000]
})

print("Pandas-on-Spark DataFrame:")
print(ps_df)

# Perform Pandas styled operations on ps_df
print('\nAverage age of employees: ',ps_df['age'].mean())

# Compute summary statistics
print("\nSummary Statistics:")
print(ps_df.describe())

# Apply a function: Add a new column with salary increment 10% increment
ps_df['IncrementedSalary'] = ps_df['salary']*1.1
print("\nIncremented Salary",ps_df["IncrementedSalary"])

# Filter Operation on pandas spark (similar to)
filtered_df = ps_df[ps_df['age']>30]
print("\nFiltered DataFrame (age > 30):")
print(filtered_df)


spark.stop()