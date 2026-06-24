from pyspark import SparkConf, SparkContext



# Setup spark objects
conf = SparkConf().setMaster('local').setAppName('AvgFriends')
sc = SparkContext(conf=conf)

def parseLine(line):
    fields = line.split(',')
    age = int(fields[2])
    numFrd = int(fields[3])
    return (age,numFrd)

# Load up data
lines = sc.textFile('C:/Users/JUS3KOR/Desktop/codes/spark course/fakefriends.csv')

#Transform data
rdd = lines.map(parseLine)

totalsByAge = rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
avgByAge = totalsByAge.mapValues(lambda x: x[0] / x[1])

res = avgByAge.collect()
res.sort()
for x in res:
    print(x)