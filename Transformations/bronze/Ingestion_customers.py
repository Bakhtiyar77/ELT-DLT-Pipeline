import dlt

#Expectations Cusomer
customers_rules = {
    "rules_1": "customer_id IS NOT NULL",
    "rules_2" : "customer_name IS NOT NULL",
}


@dlt.table(
    name = "customers_stg"
)
@dlt.expect_all_or_drop(customers_rules)
def customers_stg():
  df = spark.readStream.table("dltbahtee.source.customers")
  return df