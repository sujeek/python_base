import os
import sys
from pyspark import SparkContext
from operator import add

os.environ['SPARK_HOME'] = "/Users/zhangsan/programs/spark-2.4.0-bin-hadoop2.7"
sys.path.append("/Users/zhangsan/programs/spark-2.4.0-bin-hadoop2.7/python/")

if __name__ == "__main__":
    sc = SparkContext("local", "reduce")
    sum = sc.accumulator(0)
    my_list = [1, 2, 3, 4, 5]

    # listRdd = sc.parallelize(my_list).reduce(add)
    # print listRdd
    my_words = ["a","b","c","d","a","d","e"]
    list_rdd = sc.parallelize(my_words).cache()
    map_val = list_rdd.map(lambda x:(x,1))
    print map_val.collect()
    list_val = list_rdd.flatMap(lambda x:[(x,1)])
    print list_val.collect()
    res = list_val.reduceByKey(add).collect()
    print res