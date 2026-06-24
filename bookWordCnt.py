# from pyspark import SparkConf, SparkContext



# # Setup spark objects
# conf = SparkConf().setMaster('local').setAppName('Word Count')
# sc = SparkContext(conf=conf)

# ip = sc.textFile('C:/Users/JUS3KOR/Desktop/codes/spark course/book.txt')
# words = ip.flatMap(lambda x: x.split())
# wordsCnt = words.countByValue()

# for word , cnt in wordsCnt.items():
#     cleanWord = word.encode('ascii','ignore')
#     if(cleanWord):
#         print(cleanWord.decode() + " " + str(cnt))

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf = conf)

input = sc.textFile("C:/Users/JUS3KOR/Desktop/codes/spark course/book.txt")
words = input.flatMap(lambda x: x.split())
wordCounts = words.countByValue()

for word, count in wordCounts.items():
    cleanWord = word.encode('ascii', 'ignore')
    if (cleanWord):
        print(cleanWord.decode() + " " + str(count))