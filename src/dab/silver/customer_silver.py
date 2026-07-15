from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.table(
    name="dab.silver.customer"
)
def customer_silver():
    return (
      spark.readStream.table("customer")
           .withColumn("c_phone", regexp_replace(col("c_phone"), r"[\(\)\-]", ""))
           .withColumn("c_phone", col("c_phone").cast("long"))
           .withColumn("process_time", current_timestamp())
           .select(
                col("c_custkey").alias("customer_id"),
                col("c_name").alias("customer_name"),
                col("c_address").alias("customer_address"),
                col("c_nationkey").alias("customer_nation_key"),
                col("c_acctbal").alias("customer_account_balance"),
                col("c_mktsegment").alias("customer_market_segment"),
                col("c_comment").alias("customer_comment"),
                col("c_phone").alias("customer_phone"),
                col("process_time").alias("process_time")
           )
    )