from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from datetime import date

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection

def get_db():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        port=os.environ.get("DB_PORT", "5432"),
        database=os.environ.get("DB_NAME", "expenses"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", "3022")
    )
    return conn


# Pydantic model
class Expense(BaseModel):
    id: int = None
    title: str
    amount: float
    category: str
    date: date

@app.get("/expenses", response_model=List[Expense])
def get_expenses():
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM expenses")
    result = cur.fetchall()
    conn.close()
    return result

@app.post("/expenses", response_model=Expense)
def add_expense(expense: Expense):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO expenses (title, amount, category, date)
        VALUES (%s, %s, %s, %s) RETURNING id
        """, (expense.title, expense.amount, expense.category, expense.date))
    expense.id = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return expense

@app.put("/expenses/{id}", response_model=Expense)
def update_expense(id: int, expense: Expense):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE expenses SET title=%s, amount=%s, category=%s, date=%s
        WHERE id=%s""",
        (expense.title, expense.amount, expense.category, expense.date, id))
    conn.commit()
    conn.close()
    expense.id = id
    return expense

@app.delete("/expenses/{id}")
def delete_expense(id: int):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return {"message": "Expense deleted"}
