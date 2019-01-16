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
    schemaString = "_id drugtherapy transfusion_therapy medical_visit_record radiotherapy base_line_time _stats targetedtherapy personal_history family_history chief_complain_present_illness_history bmab bonemarrowtransplantation menstrual_marital_history immunotherapy patient_basic_information specialist_exam examination chromosome_karyotype chemotherapy"
    fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
    schema = StructType(fields)
    df = spark.read.format("json").load("/Users/zhangsan/PycharmProjects/python_data_stract/src/pds/resource/details.json")
    print(df.show())
    spark.stop()