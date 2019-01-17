from __future__ import print_function

from pyspark.sql import SparkSession

# $example on:schema_inferring$
from pyspark.sql import Row
# $example off:schema_inferring$
from pyspark.sql.types import *
import os
import sys
os.environ['SPARK_HOME'] = "/Users/zhangsan/programs/spark-2.4.0-bin-hadoop2.7"
sys.path.append("/Users/zhangsan/programs/spark-2.4.0-bin-hadoop2.7/python/")


if __name__ == "__main__":
    # $example on:init_session$
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    schemaString = "id name"
    fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
    schema = StructType(fields)
    df = spark.read.format("json").load("/Users/zhangsan/PycharmProjects/python_base/src/resource/details.json")
    print(df.show())
    spark.stop()