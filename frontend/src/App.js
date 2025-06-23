import React, { useState, useEffect} from 'react';
import axios from 'axios';

function App() {
    const [expenses, setExpenses] = useState([]);
    const [form, setForm] = useState({title: '', amount: '', category: '', date: ''});
    
    const loadExpenses = async () => {
        const res = await axios.get('/api/expenses');
        setExpenses(res.data);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        await axios.post('/api/expenses', form);
        setForm({ title: '', amount: '', category: '', date: ''});
        loadExpenses();
    };

    const deleteExpense = async (id) => {
        await axios.delete('/api/expenses/${id}');
        loadExpenses();
    };
    
    useEffect(() => {
        loadExpenses();
    },[]);

    return (
        <div>
            <h1>Expense Tracker</h1>
            <form onSubmit={handleSubmit}>
                <input value={form.title} onChange={e => setForm({...form, title: e.target.value })} placeholder="Title" required/>
                <input type="number" value={form.amount} onChange={e => setForm({...form, amount: e.target.value})} placeholder="Amount" required/>
                <input value={form.category} onChange={e => setForm({...form, category: e.target.value})} placeholder="Category" required/>
                <input type="date" value={form.date} onChange={e => setForm({ ...form, date: e.target.value })} required />
                <button type="submit">Add Expense</button>
            </form>
            <ul>
                {expenses.map(exp => (
                    <li key={exp.id}>{exp.title} - ${exp.amount}- {exp.category} <button onClick={() => deleteExpense(exp.id)}>Delete</button></li>
                ))}
            </ul>
        </div>
    );
}

export default App;