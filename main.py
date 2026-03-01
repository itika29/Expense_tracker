from fundamentalfunc import date,custom_category,display,remain_budget ;

budget = int (input("Enter your budget  :"))

date()

print("📌Enter your Expenses! \nHow much do you spent on: ")
match = {"Food":0, "Travel":0 , "Stationary":0 , "Miscellaneous":0}

for key in match:
    x = int(input(f"{key} : "))
    match[key] = x

custom_category(match)
display(match)
remain_budget(budget,match)




