# print('select an operation to perform:')
# print('''
#       1, ADD
#       2, Subtract
#       3, Multiply
#       4, Divide.
#       ''')
# operation = input('options:')
# if operation == '1':
#    num1 = input('Enter first number:')
#    num2 = input('Enter second number:')
#    print(str(int(num1) + int(num2)))
# elif operation == '2':
#     num1 = input('Enter first number:')
#     num2 = input('Enter second number:')
#     print(str(int(num1) - int(num2)))
# elif operation == '3':
#     num1 = input('Enter first number:')
#     num2 = input('Enter second number:')
#     print(str(int(num1) * int(num2)))
# elif operation == '4':
#     num1 = input('Enter first number:')
#     num2 = input('Enter second number:')
#     print(str(int(num1) / int(num2)))
# else :
#     print('Invalid Entry')
    
# print('CBT TEST QUESTION')
# print('''
#      1.Mathematics
#       2.English
#       3.Physics
#       ''')
# user = input('choice: ')
# if user == '1':
#     print('''
#           1, 3*2
#           2, 3+2
#           3, 3/2
#           ''')
# elif user == '2':
#     print('1 Choose the sentence that start with a noun')
#     print('''
#           a)Shola goes to school
#           b)my name is kunle 
#           c)i love dancing
#           ''')
#     print('2 WE_____dancing')
#     print('''
#           a)Is
#           b)Are
#           c)You
#           ''')
# elif user == '3':
#     print('1, The SI unit of displacement is')
#     print('''
#           a)Kilometer
#           b)Centimetres
#           c)Meter
#           d)Multimeters
#           ''')
#     print('2, what is the formula for workdone')
#     print('''
#           a)Mass*Force
#           b)Force*Mass
#           c)Force*distance
#           d)Acceleration/Force
#           ''')
# else:
#     print('ERROR')
    
# user = input('USSD code: ')
# if user == '*312#' :
#       print('''
#           1. Data plan
#           2. My offer
#           3. Family plan
#           4. Borrow data plan
#           ''')
#       user = input('choice: ')
#       if user == '1':
#             print('''
#               1. Daily Bundles
#               2. Weekly Bundles
#               3. Monthly Bundles
#               4. Mega Bundles
#               ''')
#             user = input('choice: ')
#             if user == '1':
#                   print('''
#                   1 #50/40MB/Daily
#                   2 #100/100MB/Daily
#                   3 #200/200MB/3days
#                   4 #350/350MB/7days
#                   ''')
#       elif user == '2':
#         print('My Airtel Offer')
#         print('''
#               1.#100/12Mins+120MB/7 days
#               2.#200/25Mins+250MB/7 days
#               3.DATA OFFERS
#               ''')

# else:
#       print('invalid code')

# 'Registration corner'
# student_list = []
# user = int(input('How many students are taking the test: '))

# student_list = [input(f'Name of student{student + 1}: ') for student in range(user)]

# for each_student in student_list:
#   print(f'\n{each_student}, its time for your test.\n')
  
#   questions = ['1. Who is president of nigeria?\na.)Buhari b.)BAT\n\n'
#                 '2. what is the capital of france\na.)Paris b.)London'
#                ]
#   answers = ['b','a']
#   score = 0
#   for questions, answers in zip(questions,answers):
#      print(questions)
#      user_ans = input('Answer: ').strip().lower()
     
#      if user_ans == answers:
#        print('correct')
#        score +=5
#      else:print
#      print(' Wrong')
  
#   print(f'Thanks for taking the test, your total score is {score}')
  
# student_database = [
#   ('Tolu','Paid'),
#   ('Wale','Half-payment'),
#   ('Tope','Not-paid')
# ]

# staff_DB = [
#   ('Femi','21'),
#   ('Yemi','62')
# ]

# visitor_DB = [
#   ('Registration'),
#   ('Tourist')
# ]

# user = input('''
#              Welcome to SQI college of ICT
             
#              Kindly clerify your identity
#              1. staff
#              2. student
#              3. Visitor
#              4. Non of the above
            
#              Option: ''').strip()

# if user == '1' or user.capitalize() == 'staff':
#     staff_id = input('ID: ').strip()
#     staff_fname = input('First name: ').strip().capitalize()
  
#     fnames = []
#     IDs = []
  
#     for fname, id in staff_DB:
#         fnames.append(fname)
#         IDs.append(id)
    
#     if staff_fname in fnames and staff_id in IDs:
#         print('Access granted 😁')
#     else:
#       print('Access declined😒')

# elif user == '2' or user.capitalize() == 'student':
#     student_fname = input('First name: ').strip().capitalize()
    
#     student_firstnames = []
#     payment_status = []
    
#     for stud, status in student_database:
#         student_firstnames.append(stud)
#         payment_status.append(status)
      
#     if student_fname in student_firstnames:
#        print(f'Welocme {student_fname}, Kindly wait let vetify your payment status')
          
#        _index = student_firstnames.index(student_fname)
#        _status = payment_status[_index]
          
#        if _status == 'Paid':
#              print(f'Welcome to class{student_fname}')
             
#        elif _status != 'Piad':
#              print(f'{student_fname}, your payment status is {_status}, Kindly visit the frontdesk for more information')
             
#     else:
#        print('Record not found try again or visit the frontdesk')
         
# elif user == '3' or user.capitalize() == 'visitor':
#      visitor_rea = input('REASON: ').strip()
      
#      reas = []
     
#      for rea in visitor_DB:
#          reas.append(rea)
         
#      if visitor_rea in reas:
#         print('Access granted 😁')
#      else:
#          print('Access declined😒')


# Food_DB = [
#   ('Rice','#2,000'),
#   ('Pasta','#3,000'),
#   ('palntain','#1,500')
# ]


# user = input('''
#              Welcome To Ikeja City Mall(ICM)
             
#              Kindly Please Place Your Order
#              1. FOOD
#              2. WEARS

#              Option: ''').strip().capitalize()

# Colors = {'Red','White','Black','Blue','Green'}

# balance = 1000
# stake = float(input('stake: '))

# while balance > 0 and balance > stake:
  
#      guess = input('guess the next color: ').strip().capitalize()
#      choosen_color = Colors.pop()
#      Colors.add(choosen_color)
     
#      if guess == choosen_color:
#          balance += 3 * stake
#          print(f'You won.\nCurrent balance is {balance}')
         
#      else:
#         balance -= stake
#         print(f'Wrong\nCurrent balance is {balance}')
        
#      user = input('press 1 to reply or # to exit: ')
#      if user == '#':
#         break
      
# else:
#     print('Insufficient balance.')
    
# print(f'Your cashout amount is {balance}')