from fundamentalfunc import Date,display,remarks;
from datetime import date 
import database

date_of_expense = Date()
database.create_table()
def get_budget() :
    curnt_budget = database.give_curntBudget()
    date_of_budget = date.today()

    if curnt_budget is None:
        budget = int(input("Enter your budget: "))
        date_of_budget = date.today()
        database.add_budget(budget, date_of_budget)
        return budget
    curnt_budget = database.give_curntBudget()
    remaining_budget = curnt_budget[2]
    
    if curnt_budget[2] is None or curnt_budget[2] <= 0 :
        budget = int(input("Enter your new budget: "))
        date_of_budget = date.today()
        database.add_budget(budget, date_of_budget)
        return budget
        
    return remaining_budget

remaining_amt = get_budget()
pre_DOB_entry = database.give_curntBudget()
DOB_entry= pre_DOB_entry[3]
# date_of_budget = DOB_entry

user_category = ["Food", "Travel","Stationary"] 

for i in range(len(user_category)):  # taking custom inputs suh that user don't have to Enter their regular expense category daily
    
    category = user_category[i]
    print(f"In {user_category[i]}")
    amount = int(input("Enter your expense: "))

    if(amount != 0): # if any day user didn't made an expense on their custom category it will not be added in expenese table
        database.add_expense(date_of_expense,amount,category)

while True :
    
    category_addup = input("Wanna add any expense (y/n) ?")
    if category_addup.lower() == "y":
        category = input("Enter category: ")
        amount = int(input("Enter your expense: "))
        database.add_expense(date_of_expense,amount,category)
        
        remaining_amt = pre_DOB_entry[2]
        break
        
    elif category_addup.lower() == "n":
        break 
    
    else :
        print(" Enter valid choice! ")
            
database.update_remaining(date_of_expense, DOB_entry)

remaining_amt = database.fetch_remaining(DOB_entry)

if remaining_amt is not None and remaining_amt <= 0:
    
    if  remaining_amt < 0 :
        exceed = database.fetch_remaining(DOB_entry)
        print(f"Your expense exceeds your budget by {exceed}")
    
    elif remaining_amt == 0 :
            print("Your budget has ended!") 
            
    while True : 
        choice = input("Wanna update your budget(y/n)?")
        if choice.lower() == 'y' :
            budget = int(input("Enter your budget: "))
            DOB_entry = date.today()
            database.add_budget(budget, date.today()) 
            pre_DOB_entry = database.give_curntBudget()
            DOB_entry = pre_DOB_entry[3]
            remaining_amt = pre_DOB_entry[2]

            break 
        
        elif choice.lower() == 'n' :
            break
        
        else :
            print("Enter valid choice!")
            
display(date_of_expense,DOB_entry)
remarks(remaining_amt)







