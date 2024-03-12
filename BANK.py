import mysql.connector as sql 
mycon = sql.connect(host = '127.0.0.1', user = 'root', password = '', database ='UBA_bankdb')
mycursor = mycon.cursor()
mycon.autocommit = True

# mycursor.execute('CREATE DATABASE UBA_bankdb')
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

fullname = input('Fullname: ')
email = input('Email: ')
account_no = input('Account no: ')
account_bal = float(input('Balance: '))
password = input('Password: ')

query = 'INSERT INTO customer_table(fullname, email, account_no, account_bal, password) VALUES (%s,%s,%s,%s,%s)'
values = (fullname, email, account_no, account_bal, password)
mycursor.execute(query, values)
print(mycursor.rowcount,'customer added successfully ')







# class Bank:
#       def __init__(self) -> None:
#             self.bankname = 'UBA'
#             self.rc_no = '203864'  
#             self.branch = 'Abuja'
            
#             self.home()
            
#       def home(self):
          
#           user = input(f'''
#              Welcome to {self.bankname} {self.rc_no}, {self.branch} branch
             
#           1. SIGN UP
#           2. SIGN IN 
#           3. EXIT
          
#           Select your option:      
#                 ''').strip()
          
#           if user == '1':
#               self.signup()
#           elif user == '2':
#               self.signin()
#           elif user == '3':
#               exit()
#           else:
#               print('Invalid Input')
              
#       def signup(self):
#           details = {''}