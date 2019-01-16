from __future__ import print_function
import os
import sys
from random import random
from operator import add
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession

os.environ['SPARK_HOME'] = "/Users/suyongjie/programs/spark-2.4.0-bin-hadoop2.7"
sys.path.append("/Users/suyongjie/programs/spark-2.4.0-bin-hadoop2.7/python/")

if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    # conf = SparkConf().setAppName("pi")
    # sc = SparkContext(conf=conf)
    # sc.setLogLevel('WARN')

    spark = SparkSession\
        .builder\
        .appName("PythonPi")\
        .getOrCreate()
    sc = spark.sparkContext
    sc.setLogLevel("WARN")

    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    n = 100000 * partitions

    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 <= 1 else 0

    count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    print("Pi is roughly %f" % (4.0 * count / n))

    spark.stop()
