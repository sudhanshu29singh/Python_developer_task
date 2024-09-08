import sqlite3
import pandas as pd

# Connect to the database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()
# Task 1:
def user_date_range(s_date,e_date):
    cursor.execute(''' SELECT * FROM users WHERE join_date BETWEEN ? AND ? ''',(s_date,e_date))

    return cursor.fetchall()
# Task 2:
def amount_spent():
    cursor.execute('''
    SELECT users.name, users.email, SUM(transactions.amount) AS total_spent
    FROM users
    JOIN transactions ON users.user_id = transactions.user_id
    GROUP BY users.user_id
    ''')
    return cursor.fetchall()
# Task 3:
def g_report():
    return amount_spent()
# Task 4:
def top3_user():
        cursor.execute('''
        SELECT users.name, users.email, SUM(transactions.amount) AS total_spent
        FROM users
        JOIN transactions ON users.user_id = transactions.user_id
        GROUP BY users.user_id
        ORDER BY total_spent DESC
        LIMIT 3
        ''')
        return cursor.fetchall()
# Task 5:
def avg_t_amount():
     cursor.execute('SELECT AVG(amount) FROM transactions')
     return cursor.fetchall()[0]
# Task 6:
def user_notransactions():
     cursor.execute('''SELECT name,email FROM users where user_id NOT IN (SELECT DISTINCT user_id FROM transactions)''')
     return cursor.fetchall()

if __name__ == "__main__":
     
     print(user_date_range('2020-09-25','2019-03-22'))

     print(amount_spent())
     print(g_report())
     print(top3_user())
     print(avg_t_amount())
     print(user_notransactions())

     connection.close()