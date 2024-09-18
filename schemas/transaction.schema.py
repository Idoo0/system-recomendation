def transactionEntity(item) -> dict:
  return {
    "id": str(item["_id"]),
    "sales_id": str(item["sales_id"]),
    "member_id": int(item["member_id"]),
    "product_name": str(item["product_name"]),
    "product_id": int(item["product_id"]),
    "_date": str(item["_date"]),
    "outlet_id": int(item["outlet_id"]),
    "name": str(item["name"]),
    "time_created": int(item["time_created"]),
  }

def transactionsEntity(entity) -> list:
  return [transactionEntity(item) for item in entity]