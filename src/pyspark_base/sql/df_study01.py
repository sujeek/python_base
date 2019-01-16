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

    sc = spark.sparkContext

    # Load a text file and convert each line to a Row.
    lines = sc.textFile("/Users/zhangsan/PycharmProjects/python_data_stract/src/pds/resource/people.txt")
    parts = lines.map(lambda l: l.split(","))
    people = parts.map(lambda p: Row(name=p[0], age=p[1]))
    schemaString = "name age"

    fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
    schema = StructType(fields)

    # Apply the schema to the RDD.
    schemaPeople = spark.createDataFrame(people, schema)

    # Creates a temporary view using the DataFrame
    schemaPeople.createOrReplaceTempView("people")
    results = spark.sql("SELECT * FROM people")
    print(results.show())
    spark.stop()