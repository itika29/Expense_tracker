from fundamentalfunc import Date, display, remarks
from datetime import date
import db_mysql
date_of_expense = Date()

db_mysql.create_table()


def get_budget():

    curnt_budget = db_mysql.give_curntBudget()
    date_of_budget = date.today()

    if curnt_budget is None:
        # for first budget entry in budget table
        # print("no budget present -> none ")
        budget = int(input("Enter your budget: "))

        db_mysql.add_budget(budget, date_of_budget)
        curnt_budget = db_mysql.give_curntBudget()

        # print(f"inserted budget {budget}")
        return budget

    remaining_budget = curnt_budget[2]

    if curnt_budget[2] is None or curnt_budget[2] <= 0:
        budget = int(input("Enter your new budget: "))
        # print(f"new budget get -> {budget}")
        date_of_budget = date.today()
        db_mysql.add_budget(budget, date_of_budget)
        return budget

    return remaining_budget


remaining_amt = get_budget()
curnt_budget = db_mysql.give_curntBudget()
DOB_entry = curnt_budget[3]
# date_of_budget = DOB_entry

user_category = ["Food", "Travel", "Stationary"]

i = 0
while i < len(user_category):
    category = user_category[i]
    print(f"In {user_category[i]}")

    try:
        amount = int(input("Enter your expense: "))
        if amount != 0:
            db_mysql.add_expense(date_of_expense, amount, category)

        i += 1

    except ValueError as e:
        print("Please enter a valid numeric value! ")
    


while True:

    category_addup = input("Wanna add any expense (y/n) ?")
    if category_addup.lower() == "y":
        category = input("Enter category: ")
        amount = int(input("Enter your expense: "))
        db_mysql.add_expense(date_of_expense, amount, category)

        # remaining_amt = curnt_budget[2]
        break

    elif category_addup.lower() == "n":
        break

    else:
        print(" Enter valid choice! ")


remaining_amt = db_mysql.fetch_remaining(DOB_entry)

if remaining_amt <= 0:

    if remaining_amt < 0:
        # exceed = db_mysql.fetch_remaining(DOB_entry)
        print(f"Your expense exceeds your budget by {remaining_amt}")

    elif remaining_amt == 0:
        print("Your budget has ended!")

    while True:
        choice = input("Wanna update your budget(y/n)?")
        if choice.lower() == 'y':
            budget = int(input("Enter your budget: "))
            # DOB_entry = date.today()
            db_mysql.add_budget(budget, DOB_entry)
            pre_DOB_entry = db_mysql.give_curntBudget()
            # DOB_entry = pre_DOB_entry[3]
            # remaining_amt = pre_DOB_entry[2]
            break

        elif choice.lower() == 'n':
            break

        else:
            print("Enter valid choice!")

else:

    display(date_of_expense, DOB_entry)
    remarks(remaining_amt)
