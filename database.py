import mysql.connector as sql 

mycon = sql.connect(host = '127.0.0.1', user = 'root', password = '', database ='bannk_2db')
mycursor = mycon.cursor()
mycon.autocommit = True

# mycursor.execute('CREATE DATABASE bannk_2db')
# mycursor.execute('SHOW DATABASE')
# for db in mycursor:
#      print(db)


# mycursor.execute(
#     'CREATE TABLE customer_table(id INT(4) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(25),email VARCHAR(25) UNIQUE, account_no VARCHAR(11) UNIQUE, account_bal FLOAT(10), data_created DATETIME DEFAULT CURRENT_TIMESTAMP)'
# )

# mycursor.execute('SHOW TABLES')
# for table in mycursor:
#     print(table)


# mycursor.execute('ALTER TABLE customer_table CHANGE id customer_id INT(4) AUTO_INCREMENT')
# mycursor.execute('ALTER TABLE customer_table ADD password VARCHAR(25)')


# fullname = input('Fullname: ')
# email = input('Email: ')
# account_no = input('Account no: ')
# account_bal = float(input('Balance: '))
# password = input('Password: ')

# query = 'INSERT INTO customer_table(fullname, email, account_no, account_bal, password) VALUES (%s,%s,%s,%s,%s)'
# values = (fullname, email, account_no, account_bal, password)
# mycursor.execute(query, values)
# print(mycursor.rowcount,'customer added successfully ')

# import pwinput as pw


# mycursor.execute('SELECT * FROM customer_table')
# details = mycursor.fetchall()
# print(details)

# mycursor.execute('SELECT fullname, account_no, account_bal FROM customer_table')
# details = mycursor.fetchall()
# print(details)

# mycursor.execute('SELECT fullname, account_no, account_bal FROM customer_table WHERE customer_id = 2')
# details = mycursor.fetchone()
# print(details)

# def signin():
#     email = input('Email: ').strip()
#     password = pw.pwinput()
    
#     query = 'SELECT fullname, account_no, account_bal FROM customer_table WHERE email = %s AND password = %s'
#     value = (email, password)
#     mycursor.execute(query,value)
#     details = mycursor.fetchone()
#     if details == None:
#         print('Incorrect password or email')
#     else:
#         print('Login successful')
        
# signin()    
   
# def signin():
#     global account_balance
#     global email
#     email = input('Email: ').strip()
#     password = pw.pwinput()
    
#     query = 'SELECT fullname, account_no, account_bal FROM customer_table WHERE email = %s AND password = %s'
#     value = (email, password)
#     mycursor.execute(query,value)
#     details = mycursor.fetchone()
#     account_balance = details[2]
    
#     if details == None:
#         print('Incorrect password or email')
#     else:
#         print('Login successful')
        
#         deposit()
        
# def deposit():
    
#     amount = float(input('Amount: '))
#     new_bal = account_balance + amount
    
#     query = 'UPDATE customer_table SET account_bal = %s WHERE email = %s'
#     values = (new_bal, email)
    
#     mycursor.execute(query,values)
#     print('Deposit succesfull, your balance is', new_bal)
# signin()    

#DELETE QUERY
# query = 'DELETE FROM customer_table WHERE customer_id = %s'
# value = (1,)
# mycursor.execute(query,value)

#DROP TABLE
# mycursor.execute('DROP TABLE customer_table')
# mycursor.execute('DROP TABLE custormer_table')

#DROP DATABASE
mycursor.execute('DROP DATABASE bannk_2db')