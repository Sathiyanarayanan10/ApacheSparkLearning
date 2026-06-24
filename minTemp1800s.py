from pyspark import SparkConf, SparkContext

# Setup Spark
conf = SparkConf().setMaster('local').setAppName('Min Temps')
sc = SparkContext(conf=conf)

#load up the data
def parseLine(line):
    fields = line.split(',')
    stationID = fields[0]
    entryType = fields[2]
    temp = float(fields[3])*0.1*(9.0/5.0)+32.0
    return(stationID,entryType,temp)

lines = sc.textFile('C:/Users/JUS3KOR/Desktop/codes/spark course/1800.csv')
parsedLines = lines.map(parseLine)

# Transform
# minTemp = parsedLines.filter(lambda x: 'TMIN' in x[1])
# minTemp = parsedLines.filter(lambda x: x[1] == 'TMIN')
maxTemp = parsedLines.filter(lambda x: 'TMAX' in x[1])

stationTemps = maxTemp.map(lambda x: (x[0],x[2]))
minTempByID = stationTemps.reduceByKey(lambda x,y: max(x,y))

# Actions
results = minTempByID.collect()

for res in results:
    print(res[0]+'\t{:.2f} F'.format(res[1]))
