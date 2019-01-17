
import os
import sys
import json
from pyspark import SparkContext
from operator import add

os.environ['SPARK_HOME'] = "/Users/zhangsan/programs/spark-2.4.0-bin-hadoop2.7"
sys.path.append("/Users/zhangsan/programs/spark-2.4.0-bin-hadoop2.7/python/")


def filter_sn(p, n_set):
    line = json.loads(p)
    sn = line.get('a')
    if sn not in n_set:
        return p

if __name__ == "__main__":
    sc = SparkContext("demo", "filter")
    sum = sc.accumulator(0)
    n_set = set()
    n_set.add(1)
    my_list = ['{"a":1}', '{"a":2}']
    listRdd = sc.parallelize(my_list).cache()
    outputs = listRdd.map(lambda p: filter_sn(p, n_set)).filter(lambda x: x is not None)
    print outputs.collect()