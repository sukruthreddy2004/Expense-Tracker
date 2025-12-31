import json
import os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"expenses": []}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_expense():
    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("\nAmount must be greater than zero.\n")
            return
    except ValueError:
        print("\nInvalid amount. Please enter a number.\n")
        return

    data = load_data()
    data["expenses"].append({"category": category, "amount": amount})

    save_data(data)
    print("\nExpense saved\n")


def view_expenses():
    data = load_data()
    if not data["expenses"]:
        print("\nNo expenses recorded yet.\n")
        return
    
    print("\nAll Expenses:")
    for exp in data["expenses"]:
        print(f"- {exp['category']}: ₹{exp['amount']}")
    print()

def view_total():
    data = load_data()
    total = sum(exp["amount"] for exp in data["expenses"])
    print(f"\nTotal spent: ₹{total}\n")

def view_by_category():
    data = load_data()
    category_totals = {}

    for exp in data["expenses"]:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    print("\nTotal by Category:")
    for cat, amt in category_totals.items():
        print(f"- {cat}: ₹{amt}")
    print()

def menu():
    while True:
        print("----- EXPENSE TRACKER -------")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. View Total by Category")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            view_by_category()
        elif choice == "5":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid. Try again.\n")

if __name__ == "__main__":
    menu()
