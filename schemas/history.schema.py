def historyEntity(item) -> dict:
  return {
    "id": str(item["_id"]),
    "last_update": str(item["last_update"])
  }

def historiesEntity(entity) -> list:
  return [historyEntity(item) for item in entity]