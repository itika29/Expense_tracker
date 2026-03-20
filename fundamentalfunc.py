def date():

    date_in= input("Enter date (dd-mm-yyyy): ")
    split_Date = date_in.split("-")
    date_format = list(map(int,split_Date))
    month = {1:31,2:30,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    def leap_year(y : int) -> bool:
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) :
            return True
        return False
    
    if date_format[2] > 2026 :
        print("Inavlid year!")
        date()

    elif date_format[1] > 12 :
        print ("Invalid month!")
        date()

    elif leap_year(date_format[2]) and date_format[1] == 2  and date_format[0] > 29 :
        print("Invalid date!")
        date()
    
    elif not leap_year(date_format[1]) and date_format[1] == 2  and date_format[0] > 28 :
        print("Invalid date!")
        date()
    
    elif date_format[1] != 2 and date_format[0] > month[date_format[1]] :
        print("Invalid date!")
        date()
    else :
        pass


def custom_category(match : dict) :
    
    while True:
        choice= input("Do you want to enter any particular expense category?(y/n) ")
        if (choice.lower()=="y") :
            N_category = input("Enter category name :")
            N_expense = int (input(f"Enter {N_category}'s expense \n{N_category} :"))
            match[N_category] = N_expense
        elif choice.lower() == "n" :
            break
        else:
            print("Enter valid choice!")


def display(match : dict):
    print (f'''
🥁 Running Expense Tracker !
🎯 Summarising user response
📑 Expenses by category
           
🍔 Food : {match["Food"]} 
🧩 Stationary : { match["Stationary"] }
📍 Travel : {match["Travel"]}
💅 Miscellaneous : {match["Miscellaneous"]} ''')
    key= list(match.keys())
    for i in range(4,len(key)):
        print(f"✨ {key[i]} : {match[key[i]]}")
       


def remain_budget(budget,match):
    
    budget  = budget- sum(match.values())
    if budget > ((1/2)*budget ):
        print(f"Dear! \n🎉 {budget} amount is left now!")
    elif budget == ((1/2)*budget):
        print(f"Dear! \n📌 You have half of your budget leftover i.e {budget}")
    elif budget >= (1/4)*budget and budget <= (1/2)*budget :
        print(f"Dear! \n🥲 You have {budget} amount remaining ")
    elif budget == 0:
        print("Shit! your budget end!..add up your bugdet next time to run expense analyzer!")
    elif budget < 0 :
        print(f"So impractical! you expend more than your budget {budget}..May be you forgot to append more amount on your budget ")
    else :
        print(f"heyy! you have {budget} amount remaining only 😓")

    

# def budget_end(budget) :
#     if budget <=0 :
#         print("no more budget...add up ur budget to run analyzer!")
#         return True
#     else:
#         return False


