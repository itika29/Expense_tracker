# import database
from datetime import datetime
import calendar
import db_mysql


def Date():
    now = datetime.now()
    date_in = input(
        "Enter date or press Enter for today's date(YYYY-MM-DD): ").strip()
    if date_in == "":
        date_in = now.date()

    # print(f"input received {date_in} ")
    # checks date validity

    else:
        split_Date = date_in.split("-")
        if "" in split_Date or len(split_Date) != 3:
            print("Invalid format!")
            Date()
        date_format = list(map(int, split_Date))
        print(date_format)

        if date_format[0] <= now.year and date_format[1] <= 12:
            lastday = calendar.monthrange(date_format[0], date_format[1])[1]
            if date_format[0] > lastday:
                print("Invalid input")

        else:
            print("Invalid Input")

    return date_in


def display(date_of_expense, date_of_budget):

    expenditure = db_mysql.fetch_expense(date_of_expense)
    remains = db_mysql.fetch_remaining(date_of_budget)
    print(f""" 
          

          🥁 Running Expense Tracker !
          🎯 Summarising user response
           The total amount you spent today : {expenditure}
           Remaining budget in your wallet : {remains}


    """)


def total_moneyspent(remaining_amt):

    curntBudget = db_mysql.give_curntBudget()
    # print(f"remaining amt : {remaining_amt}")
    total_Spent = curntBudget[1]-remaining_amt
    # print(f"current_budget: {curntBudget[1]} ")
    # print(f"total_Spent: {total_Spent} ")
    moneySpent_percent = (total_Spent / curntBudget[1]) * 100
    # print(f"money spent % : {moneySpent_percent}")
    # print(moneySpent_percent)
    return moneySpent_percent


def total_dayspent():

    totaldays = db_mysql.day_spent()   # end day of month

    # print(f"total month days : {totaldays}")
    curntdate = db_mysql.return_latestDate()
    curntdate = str(curntdate)
    split_date = curntdate.split("-")
    List_of_date_ele = list(map(int, split_date))
    # print(f"curnt date : {List_of_date_ele[2]}")
    daySpent_percent = (List_of_date_ele[2] / totaldays) * 100
    # print(daySpent_percent)
    # print(f"day spent % : {daySpent_percent}")
    return daySpent_percent


def remarks(remaining_amt):
    daysSpent = total_dayspent()
    moneySpent = total_moneyspent(remaining_amt)
    difference = moneySpent - daysSpent
    if difference <= 10 and difference >= -10:
        print("🟢You’re on track with your monthly budget 👍")

    elif difference > 10 and difference <= 25:
        print("🟡You’re spending slightly faster than planned—monitor expenses.")

    elif difference > 25:
        print("🔴You are overspending significantly—review your expenses urgently.")

    elif difference >= -25 and difference < -10:
        print("🔵Good control! You’re spending below your budget pace")

    elif difference < -25:
        print("🟣You’re saving aggressively this month.")
