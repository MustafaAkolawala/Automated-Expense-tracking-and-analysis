import React, { useState, useEffect } from 'react';
import { getExpenses } from '../api/api';

const ExpenseList = () => {
  const [expenses, setExpenses] = useState([]);

  useEffect(() => {
    async function fetchExpenses() {
      const data = await getExpenses();
      setExpenses(data);
    }
    fetchExpenses();
  }, []);

  return (
    <div>
      <h2>Expenses</h2>
      <ul>
        {expenses.map((expense, index) => (
          <li key={index}>
            {expense.description}: ${expense.amount} - {expense.category}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ExpenseList;
