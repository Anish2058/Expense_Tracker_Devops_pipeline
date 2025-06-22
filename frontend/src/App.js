import React, { useState, useEffect} from 'react';
import axios from 'axios';

function App() {
    const [expenses, setExpenses] = useState([]);
    const [form, setForm] = useState({title: '', amount: '', category: '', date: ''});
}