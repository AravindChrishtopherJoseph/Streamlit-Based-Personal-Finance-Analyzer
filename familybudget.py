

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
def load_data(file):
    return pd.read_csv(file)

# Budgeting logic
def calculate_budget(df):
    # Calculate totals
    income = df['Credit Amount'].sum()
    expenses = df['Debit Amount'].sum()
    savings = income - expenses
    
    return income, expenses, savings

# Streamlit app
def main():
    st.title("Family Budgeting App")
    file = st.file_uploader("Upload bank statement file")
    
    if file:
        df = load_data(file)
        income, expenses, savings = calculate_budget(df)
        
        st.write("Budget Summary:")
        st.write(f"Income: ${income:.2f}")
        st.write(f"Expenses: ${expenses:.2f}")
        st.write(f"Savings: ${savings:.2f}")
        
        # Visualize budget breakdown
        fig, ax = plt.subplots()
        ax.bar(['Income', 'Expenses', 'Savings'], [income, expenses, savings])
        ax.set_xlabel('Budget Category')
        ax.set_ylabel('Amount ($)')
        ax.set_title('Budget Breakdown')
        st.pyplot(fig)

        # Category-wise expenses
        expense_df = df.groupby('Category')['Debit Amount'].sum().reset_index()
        fig, ax = plt.subplots()
        ax.bar(expense_df['Category'], expense_df['Debit Amount'])
        ax.set_xlabel('Category')
        ax.set_ylabel('Expenses ($)')
        ax.set_title('Category-wise Expenses')
        ax.tick_params(axis='x', rotation=90)
        st.pyplot(fig)

if __name__ == "__main__":
    main()