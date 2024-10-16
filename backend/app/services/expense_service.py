from app.core.config import db
from app.models.expense import Expense
from bson import ObjectId

async def create_expense(expense_data: dict) -> dict:
    new_expense = await db.expenses.insert_one(expense_data)
    created_expense = await db.expenses.find_one({"_id": new_expense.inserted_id})
    return created_expense

async def get_expenses():
    expenses = await db.expenses.find().to_list(length=100)
    return expenses

async def delete_expense(expense_id: str):
    result = await db.expenses.delete_one({"_id": ObjectId(expense_id)})
    return result.deleted_count > 0
