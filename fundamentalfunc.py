import database
from datetime import date

def Date():

    date_in = input("Enter date or press Enter for today's date(YYYY-MM-DD): ")
    # checks date validity 
    split_Date = date_in.split("-")
    date_format = list(map(int,split_Date))
    month = {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    def leap_year(y : int) -> bool:
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) :
            return True
        return False
    
    if date_format[0] > 2026 :
        print("Inavlid year!")
        Date()

    elif date_format[1] > 12 :
        print ("Invalid month!")
        Date()

    elif leap_year(date_format[0]) and date_format[1] == 2  and date_format[2] > 29 :
        print("Invalid date!")
        Date()
    
    elif not leap_year(date_format[0]) and date_format[1] == 2  and date_format[2] > 28 :
        print("Invalid date!")
        Date()
    
    elif date_format[1] != 2 and date_format[2] > month[date_format[1]] :
        print("Invalid date!")
        Date()
    else :
        pass
    
    if date_in == "":
        date_in = date.today()
        
    return date_in

def display(date_of_expense,date_of_budget):

    expenditure = database.fetch_expense(date_of_expense)
    remains = database.fetch_remaining(date_of_budget)
    print(f""" 
          

          🥁 Running Expense Tracker !
          🎯 Summarising user response
           The total amount you spent today : {expenditure}
           Remaining budget in your wallet : {remains}


    """)

def total_moneyspent (remaining_amt):
    curntBudget = database.curntbudget()
    total_Spent = curntBudget[0]-remaining_amt
    moneySpent_percent = (total_Spent/curntBudget[0]) * 100 
    
    return moneySpent_percent

def total_dayspent ():
    days = database.day_spent()
    curntdate = days[0]
    totaldays = days[1]
    daySpent_percent = (curntdate / totaldays)* 100
    
    return daySpent_percent

def remarks(remaining_amt):
    daysSpent = total_dayspent()
    moneySpent = total_moneyspent(remaining_amt)
    difference = moneySpent - daysSpent
    if difference <= 10 and difference >= -10:
        print("🟢You’re on track with your monthly budget 👍")
        
    elif difference > 10 and difference <= 25:
        print("🟡You’re spending slightly faster than planned—monitor expenses.")
        
    elif difference > 25 :
        print("🔴You are overspending significantly—review your expenses urgently.")
        
    elif difference >= -25 and difference < -10:
        print("🔵Good control! You’re spending below your budget pace")        
        
    elif difference < -25 :
        print("🟣You’re saving aggressively this month.")
   
    
 

        
