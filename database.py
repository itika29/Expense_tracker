import sqlite3 

def connect():
    return sqlite3.connect("expenses.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    #Expenses table
    cursor.execute(""" CREATE TABLE IF NOT EXISTS EXPENSES(
                   S_No INTEGER PRIMARY KEY AUTOINCREMENT,
                   Date text,
                   Category text NOT NULL,
                   Expense Integer 
                   );
                   
                   """) 
               
    #budget table
    cursor.execute( """CREATE TABLE IF NOT EXISTS BUDGET(
                   ID INTEGER PRIMARY KEY,
                   total_amount INT,
                   REMAINING_BUDGET INT,
                   Entry_date text      
                   ); 
                   """)
    
    conn.commit()
    conn.close()  

# def add_clm():
#     conn = connect()
#     cursor = conn.cursor()
#     cursor.execute("ALTER TABLE BUDGET ADD COLUMN Entry_date text")


def add_budget(budget,date_of_budget):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO BUDGET(total_amount,remaining_budget,Entry_date) VALUES (?,?,?) " ,(budget,budget,date_of_budget)
    )
    conn.commit()
    conn.close() 

def add_expense(date,amount,category) :
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO EXPENSES (Expense,Category,Date) VALUES (?,?,?)",(amount,category,date))
    conn.commit()
    conn.close()

def reset_remaining_budget(date_of_budget):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE BUDGET
        SET remaining_budget = total_amount
        WHERE ID = (
            SELECT ID
            FROM BUDGET
           
            ORDER BY ID DESC
            LIMIT 1
        )
        """
    )
    conn.commit()
    conn.close()

def update_remaining(date_of_expense, date_of_budget):
    conn = connect()
    cursor = conn.cursor()
    amt_expend = fetch_expense(date_of_expense)
    amt_expend = 0 if amt_expend is None else amt_expend
    cursor.execute(
        """
        UPDATE BUDGET
        SET remaining_budget = remaining_budget - ?
        WHERE ID = (
            SELECT ID
            FROM BUDGET
            ORDER BY ID DESC
            LIMIT 1
        )
        """,
        (amt_expend,),
    )
    conn.commit()
    conn.close()

def give_curntBudget():
    
    conn =connect()
    cursor = conn.cursor()
    cursor.execute("SELECT ID,total_amount, remaining_budget,Entry_date FROM budget ORDER BY ID DESC LIMIT 1")
    lastRow = cursor.fetchone()
    conn.close()
    
    return lastRow

def fetch_expense(date_of_expense) :
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(Expense) FROM EXPENSES WHERE Date = ?",(date_of_expense,))
    expenditure = cursor.fetchone() 
    conn.commit()
    conn.close()
    return expenditure[0]

def fetch_remaining(date_of_budget):
    conn =connect()
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT total_amount, remaining_budget
        FROM BUDGET
        WHERE Entry_date = ?
        ORDER BY ID DESC
        LIMIT 1
        """,
        (date_of_budget,),
    )
    Expend = cursor.fetchone()
    conn.commit()
    conn.close()
    if Expend is None:
        return None
    if Expend[1] is None:
        reset_remaining_budget(date_of_budget)
        return Expend[0]
    return Expend[1]

# Will return the current budget for calc % money spent 
def curntbudget():
    conn =connect()
    cursor = conn.cursor()
    cursor.execute("SELECT total_amount FROM BUDGET ORDER BY ID DESC LIMIT 1")
    curntBudget = cursor.fetchone()
    conn.close
    
    return curntBudget

def day_spent():
    conn =connect()
    cursor = conn.cursor()
    # will return today date , total days 
    cursor.execute ("""SELECT 
                    CAST (strftime('%d' , 'now') AS INTEGER),  
                    CAST (strftime('%d' ,date('now','start of month','+1 month','-1 day'))AS INTEGER)
                    """)
    
    days = cursor.fetchone()
    return days