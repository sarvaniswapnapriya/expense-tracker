import csv
import os

EXPENSE_FILE = 'data/expenses.csv'

# Ensure the expense file exists
if not os.path.exists(EXPENSE_FILE):
    with open(EXPENSE_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Description', 'Amount'])

def get_expenses():
    """Retrieve all expenses from the CSV file."""
    expenses = []
    with open(EXPENSE_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        expenses = list(reader)
    return expenses

def add_expense(description, amount):
    """Add a new expense to the CSV file."""
    with open(EXPENSE_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([description, amount])
