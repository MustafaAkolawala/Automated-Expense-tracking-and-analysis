from fastapi import APIRouter, HTTPException
from app.services.expense_service import create_expense, get_expenses, delete_expense
from app.models.expense import Expense

router = APIRouter()

@router.post("/expenses/")
async def create_expense_route(expense: Expense):
    expense_data = expense.dict()
    created_expense = await create_expense(expense_data)
    return created_expense

@router.get("/expenses/")
async def get_expenses_route():
    expenses = await get_expenses()
    return expenses

@router.delete("/expenses/{expense_id}")
async def delete_expense_route(expense_id: str):
    deleted = await delete_expense(expense_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Expense deleted"}