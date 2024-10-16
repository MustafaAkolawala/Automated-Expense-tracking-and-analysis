from fastapi import FastAPI
from app.api import auth, expenses, bank_statement

app = FastAPI()

# Register routes
app.include_router(auth.router)
app.include_router(expenses.router)
app.include_router(bank_statement.router)

@app.get("/")
def root():
    return {"message": "Expense Tracker API"}
