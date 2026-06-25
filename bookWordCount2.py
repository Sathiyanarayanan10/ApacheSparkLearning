from pyspark.sql import SparkSession
from pyspark.sql import functions as func

spark = SparkSession.builder.appName('WordCount').getOrCreate()

# read the text
inputDF = spark.read.text('book.txt')

# using explode its like a flatmap() and \\W+ is a regular expression that splits up based on spaces, punctuations etc.
words = inputDF.select(func.explode(func.split(inputDF.value, "\\W+")).alias("word"))
wordsWithoutEmptyString = words.filter(words.word != "")

# Normalize everything to lowercase
lowercaseWords = wordsWithoutEmptyString.select(func.lower(wordsWithoutEmptyString.word).alias("word"))

# Count up the occurrences of each word
wordCounts = lowercaseWords.groupBy("word").count()

# Sort by counts
wordCountsSorted = wordCounts.sort("count")

# Show the results.
wordCountsSorted.show(wordCountsSorted.count())

spark.stop()