import dlt


#Products Rules 
product_rules = {
  "rules_1": "product_id IS NOT NULL",
  "rules_2": "price >= 0"
}

@dlt.table(
    name = "products_stg"
)
@dlt.expect_all(product_rules)
def products_stg():
  df = spark.readStream.table("dltbahtee.source.products")
  return df