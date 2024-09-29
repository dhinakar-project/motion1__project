import datetime

# Dictionary to store expense data
expense_data = {}

# Function to add a new expense
def add_expense(date, category, description, amount):
    if date not in expense_data:
        expense_data[date] = []
    expense_data[date].append({
        'category': category,
        'description': description,
        'amount': amount
    })
    print(f"Expense added: {description} - ${amount} in {category} on {date}.")

# Function to show total expenses by category
def view_category_summary():
    category_summary = {}
    for date, expenses in expense_data.items():
        for expense in expenses:
            category = expense['category']
            amount = expense['amount']
            category_summary[category] = category_summary.get(category, 0) + amount
    
    print("\nCategory-wise Expenditure:")
    for category, total in category_summary.items():
        print(f"{category}: ${total:.2f}")

# Function to view monthly summary
def view_monthly_summary(month, year):
    monthly_total = 0
    for date, expenses in expense_data.items():
        expense_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        if expense_date.month == month and expense_date.year == year:
            for expense in expenses:
                monthly_total += expense['amount']
    
    print(f"\nTotal Expenses for {year}-{month:02d}: ${monthly_total:.2f}")

# Main program logic
def main():
    print("Welcome to the Expense Tracker!")
    
    while True:
        print("\nOptions:")
        print("1. Add new expense")
        print("2. View category-wise summary")
        print("3. View monthly summary")
        print("4. Exit")
        
        choice = input("Please select an option (1-4): ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (e.g., Food, Transport, Entertainment): ")
            description = input("Enter a brief description: ")
            try:
                amount = float(input("Enter the amount: "))
                add_expense(date, category, description, amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        
        elif choice == '2':
            view_category_summary()
        
        elif choice == '3':
            try:
                month = int(input("Enter the month (1-12): "))
                year = int(input("Enter the year (e.g., 2024): "))
                view_monthly_summary(month, year)
            except ValueError:
                print("Invalid input for month/year. Please enter valid numbers.")
        
        elif choice == '4':
            print("Thank you for using the Expense Tracker!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
