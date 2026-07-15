from pyspark import pipelines as dp
from pyspark.sql.functions import *


# Please edit the sample below


@dp.table(
    name="customer"
)
def bronze():
    return (
        spark.readStream.table("samples.tpch.customer")
             .withColumn("ingestion_time", current_timestamp())
    )