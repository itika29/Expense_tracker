from fundamentalfunc import date,custom_category,display,remain_budget ;

budget = int (input("Enter your budget  :"))
# date_in= input("Enter date (dd-mm-yyyy): ") = 0 
date()
print("📌Enter your Expenses! \nHow much do you spent on: ")
# Food = int(input("Food : "))
#     Stationary = int(input( "Stationary :"))
#     Travel = int(input( "Travel :"))
#     Miscellaneous = int(input( "Miscellaneous :"))

match = {"Food":0, "Travel":0 , "Stationary":0 , "Miscellaneous":0}

for key in match:
    x = int(input(f"{key} : "))
    match[key] = x
    # Stationary = int(input( "Stationary :"))
    # Travel = int(input( "Travel :"))
    # Miscellaneous = int(input( "Miscellaneous :"))
custom_category(match)
display(match)
remain_budget(budget,match)




