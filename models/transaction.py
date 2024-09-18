from pydantic import BaseModel

class Transaction(BaseModel):
  sales_id: str
  member_id: int
  product_name: str
  product_id: int
  _date: str
  outlet_id: int
  name: str
  time_created: int
