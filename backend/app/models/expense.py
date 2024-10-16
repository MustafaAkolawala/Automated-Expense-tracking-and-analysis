from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class Expense(BaseModel):
    id: Optional[str]
    user_id: str
    amount: float
    category: str
    description: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }