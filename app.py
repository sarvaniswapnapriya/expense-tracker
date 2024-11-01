from flask import Flask, render_template, request, redirect, url_for
from expenses import get_expenses, add_expense  # Import the functions
import os

app = Flask(__name__)

@app.route('/')
def index():
    expenses = get_expenses()  
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense_route():
    description = request.form.get('description')
    amount = request.form.get('amount')
    add_expense(description, amount)  # Use the function to add an expense
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
