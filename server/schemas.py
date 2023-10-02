from pydantic import BaseModel

class CreditCard(BaseModel):
    number: str
    expiration_date: str
    cvv: str
    name: str

