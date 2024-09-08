import sqlite3
# Connect to the SQLite database
Connection = sqlite3.connect('example.db')
cursor = Connection.cursor()
# Delete existing data
cursor.execute('DELETE FROM users')
cursor.execute('DELETE FROM transactions')
# Sample data
users_data =[
    (1,'Amit','amit@example.com','2020-09-25'),
    (2,'Neha','neha@example.com','2019-03-22'),
    (3,'Suman','suman@example.com','2020-09-25'),
    (4,'Arjun','arjun@example.com','2020-09-21'),
    (5,'Sachin','sachin@example.com','2022-09-21'),

]
# Sample data
transaction_data = [
    (1,1,250.00,'2020-09-25'),
    (2,2,150.00,'2019-03-22'),
    (3,1,350.00,'2020-09-21'),
    (4,3,450.00,'2020-09-25'),
    (5,4,650.00,'2021-07-01'),
    (6,2,250.00,'2022-07-01'),
]
# Insert into 'users'
cursor.executemany('''INSERT INTO users(user_id,name,email,join_date) VALUES (?,?,?,?) ''', users_data)
# Insert into 'transactions'
cursor.executemany('''INSERT INTO transactions (transaction_id,user_id,amount,transaction_date)
                    VALUES (?,?,?,?) ''',transaction_data)
Connection.commit()
Connection.close()

print("data inserted successfully...")
