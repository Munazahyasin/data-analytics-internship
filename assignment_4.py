import csv
import os

FILE_NAME = "expenses.csv"


# Create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])


# Add a new expense
def add_expense():
    print("\n===== ADD EXPENSE =====")

    date = input("Enter date (DD-MM-YYYY): ").strip()

    if date == "":
        print("Date cannot be empty.")
        return

    category = input("Enter category: ").strip()

    if category == "":
        print("Category cannot be empty.")
        return

    # Validate amount
    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    note = input("Enter note (optional): ").strip()

    # Save expense to CSV
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("Expense added successfully!")


# View all expenses
def view_expenses():
    print("\n===== ALL EXPENSES =====")

    total = 0

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            print(f"{'Date':<15}{'Category':<15}{'Amount':<12}{'Note'}")
            print("-" * 60)

            for expense in expenses:
                date = expense["Date"]
                category = expense["Category"]
                amount = float(expense["Amount"])
                note = expense["Note"]

                print(f"{date:<15}{category:<15}{amount:<12.2f}{note}")

                total += amount

            print("-" * 60)
            print(f"Total Amount Spent: ₹{total:.2f}")

    except FileNotFoundError:
        print("Expense file not found.")


# Category-wise spending summary
def category_summary():
    print("\n===== CATEGORY-WISE SUMMARY =====")

    category_totals = {}

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for expense in reader:
                category = expense["Category"]
                amount = float(expense["Amount"])

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

            if not category_totals:
                print("No expenses recorded yet.")
                return

            for category, total in category_totals.items():
                print(f"{category}: ₹{total:.2f}")

    except FileNotFoundError:
        print("Expense file not found.")


# Main menu
def main():
    create_file()

    while True:
        print("\n==============================")
        print("      EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category-wise Summary")
        print("4. Exit")
        print("==============================")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            category_summary()

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


# Start the program
if __name__ == "__main__":
    main()