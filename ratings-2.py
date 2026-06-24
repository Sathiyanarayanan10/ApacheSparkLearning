from pyspark import SparkConf, SparkContext
import collections

#set up spark context
config = SparkConf().setMaster('local').setAppName('Ratings Counter')
sc = SparkContext(conf= config)

#load up the data
lines = sc.textFile("C:/Users/JUS3KOR/Desktop/codes/spark course/ml-100k/u.data")

#Transform data
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()

#python display code
resultCnt = collections.OrderedDict(sorted(result.items()))

for key,val in resultCnt.items():
    print('%s %i'%(key,val))
