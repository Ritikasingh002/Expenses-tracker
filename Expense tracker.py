# Expense tracker project
expenses = []  # list of all expenses in form of dictionary

print("Welcome to expense tracker : Kharcha kam kiya karo")

# Add expenses
while True:
    print("\n=== MENU ===")
    print("1. Add Expenses")
    print("2. View all the Expenses")
    print("3. View total kharcha")
    print("4. Exit")

    choice = int(input("Please Enter your choice: "))

    # 1. Add Expenses
    if choice == 1:
        date = input("Enter the date: ")
        category = input("Enter the category (e.g: food, travel etc): ")
        description = input("Give all the detail: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("\nDONE bro. Expense added successfully!")

    # 2. View all Expenses
    elif choice == 2:
        if len(expenses) == 0:
            print("No Expenses Added. Jao pahle kharcha karo kuchh")
        else:
            print("==== This is your total expenses ===")
            count = 1
            for each_expense in expenses:
                print(f"Expense {count} -> {each_expense['date']}, {each_expense['category']}, {each_expense['description']}, {each_expense['amount']}")
                count += 1

    # 3. View Total Spending
    elif choice == 3:
        total = 0
        for each_expense in expenses:
            total += each_expense["amount"]
        print("\nTOTAL EXPENSES =", total)

    # 4. Exit
    elif choice == 4:
        print("Thank you for using this Expense tracker!")
        break

    else:
        print("Invalid choice, Try again")