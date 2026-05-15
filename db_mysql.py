import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="REMEMBERIT",   # put your MySQL password
        database="expense_tracker"
    )
    cursor = conn.cursor()
    # print("Connected successfully!")

except Exception as e:
    print("Error:", e)


def create_table():

    cursor.execute("""
                CREATE TABLE if not exists expenses (
                    S_NO INT AUTO_INCREMENT PRIMARY KEY,
                    date DATE ,
                    category varchar(20),
                    Expense int 
                );
                
                """)

    cursor.execute("""
                CREATE TABLE if not exists budget (
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    date DATE ,
                    BUDGET INT,
                    REMAINING_AMT int 
                );
                
                """)
    conn.commit()


def give_curntBudget():

    cursor.execute(
        "SELECT ID,budget, remaining_amt,date FROM budget ORDER BY ID DESC LIMIT 1;")
    lastRow = cursor.fetchone()
    # print(f"give current_budget returns {lastRow}")
    return lastRow


def add_budget(budget, date_of_budget):
    print(f"{budget}, {date_of_budget}")
    cursor.execute("""
                   INSERT INTO budget (date,budget,remaining_amt) VALUES(%s,%s,%s);
                   """, (date_of_budget, budget, budget))
    conn.commit()

    cursor.execute("SELECT * from BUDGET ORDER BY Id desc ")
    selected = cursor.fetchone()

    # print(selected)

    # print("add_budget opeartion completed")


def add_expense(date, amount, category):
    cursor.execute(
        "INSERT INTO EXPENSES (Expense,Category,Date) VALUES (%s,%s,%s);", (amount, category, date))
    conn.commit()


def fetch_remaining(date_of_budget):

    cursor.execute(
        """
        SELECT BUDGET, remaining_amt
        FROM BUDGET
        WHERE date = %s
        ORDER BY ID DESC
        LIMIT 1 ;
        """,
        (date_of_budget,),
    )
    Expend = cursor.fetchone()
    # conn.commit()

    if Expend is None:
        return None
    # if Expend[1] is None:

    #     return Expend[0]
    return Expend[1]


def fetch_expense(date_of_expense):

    cursor.execute(
        "SELECT SUM(Expense) FROM EXPENSES WHERE Date = %s;", (date_of_expense,))
    expenditure = cursor.fetchone()
    conn.commit()

    return expenditure[0]


def day_spent():

    # will return current date , total days
    cursor.execute(" SELECT DAY(LAST_DAY(CURDATE()));")

    Total_days = cursor.fetchone()
    # print(f"total days: {Total_days}")
    return Total_days[0]


def return_latestDate():
    # WILL RETURN LATEST DATE OF EXPENSE
    cursor.execute("SELECT date FROM expenses ORDER BY S_NO DESC LIMIT 1;")
    latest_date_of_expense = cursor.fetchone()
    # print(latest_date_of_expense[0])
    return latest_date_of_expense[0]



# def update_remaining(date_of_expense, date_of_budget):
#     conn = connect()
#     cursor = conn.cursor()
#     amt_expend = fetch_expense(date_of_expense)
#     amt_expend = 0 if amt_expend is None else amt_expend
#     cursor.execute(
#         """
#         UPDATE BUDGET
#         SET remaining_budget = remaining_budget - ?
#         WHERE ID = (
#             SELECT ID
#             FROM BUDGET
#             ORDER BY ID DESC
#             LIMIT 1
#         )
#         """,
#         (amt_expend,),
#     )
#     conn.commit()
#     conn.close()

# def update_remaining():
    # cursor.execute("""

    #    CREATE TRIGGER if not exists update_remaining_amt
    #    AFTER INSERT
    #    ON Expenses
    #    FOR EACH ROW
    #    BEGIN
    #    UPDATE budget
    #    SET remaining_amt = remaining_amt - NEW.expense
    #    ORDER BY ID DESC
    #    LIMIT 1 ;
    #    END;

    #                """)
    # conn.commit()

