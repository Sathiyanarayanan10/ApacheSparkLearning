from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('Shop Sales')
sc = SparkContext(conf=conf)

lines = sc.textFile('C:/Users/JUS3KOR/Desktop/codes/spark course/customer-orders.csv')

parsedLines = lines.map(lambda x: x.split(','))

customerAmount = parsedLines.map(lambda x: (x[0], float(x[2])))

totals = customerAmount.reduceByKey(lambda x, y: x + y)

for customer, total in sorted(totals.collect()):
    print(customer, round(total, 2))