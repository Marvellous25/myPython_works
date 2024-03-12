# print("My name is Marvellous")
# print('Welcome ' + 'back')
# first_name_='Marvellous'
# last_name='Anu'
# Age=12
# # print('my name is ',  first_name_ ,  last_name ,  'And i am ',   Age,  'years old')
# print(f'my name is {first_name_} {last_name} And i am {Age} years old ')
# # print('my name is ' , last_name)
# print('my name is {} {}'. format(first_name_, last_name))
# val =int(6)
# val = True
# list_python_student = ['Favour', 'Joshua', 'Me', 23, 45, True, ['yam','rice']]
# print(list_python_student)
# print(list_python_student[1])
# print(list_python_student[-1][0])
# my_tuple =['Favour', 'Joshua', 'Me', 23, 45, True, ['yam','rice'], ('password','username')]
# print(my_tuple[-1])
# print(my_tuple[-1][0])
# print(my_tuple[-1][0][4])
# my_range = range(21)
# print(my_range)
# print(tuple(my_range))
# print(list[my_range])
# student_detials = {'Nmae':'Toluwanimi', 'Gender':'Female', 'Dept':'AI'}
# print(student_detials)
# my_set = {5,7,3,4,2,4,3,34}
# my_set2 = {'Titi', 'Kunle','Bisi'}
# print(my_set2)
# print(list_python_student[1])
# print(list_python_student[-1][0])
# my_tuple =['Favour', 'Joshua', 'Me', 23, 45, True, ['yam','rice'], ('password','username')]
# Airline = 'starlink'
# print(Airline)

# print(''' 
#       1. ADD
#       2. SUBTRACT
#       3. DIVISION
#       4. MULTIPLY
#       ''')
# user = input('option: ')
# first_value = float(input('first value: '))
# second_value = float(input('second value: '))
# if user == '1':
#     res = first_value + second_value
#     print(f'Answer: {res}')
    
# elif user == '2':
#      res = first_value - second_value
#      print(f'Answer: {res}')
# elif user == '3':
#      res = first_value / second_value
#      print(f'Answer: {res}')
# elif user == '4':
#      res = first_value * second_value
#      print(f'Answer: {res}')
# else:
#     print('invalid command')

# user = input('USSD code: ')
# if user == '*312#' :
#     print('''
#           1. Data plan
#           2. check balance
#           ''')
#     user = input('choice: ')
#     if user == '1':
#         print('''
#               DATA PLAN
#               1. Daily plan
#               2. Weekly plan
#               3. Monthly plan
#               ''')
#     elif user == '2':
#         print('CHECK BALANCE')
        
#     else:
#         print('invalid USSD code')
        
        
# name = 'MARY has a little lamb'
# print(name.capitalize())
# print(name.lower())
# print(name.upper())
# print(name.title())

# user = input('Autorenewal?, yes or no? ').strip().capitalize()
# if user == 'Yes':
#     print('Autorenew successful')
# else:
#     print('Autorenew declined')
# name = 'Mary has a little lamb. she loves food'
# print(name.split())
# word = name.split() 
# print(word)

# word_join = ''.join(word)
# print(word_join)
# print(name.startswith('m'))
# print(name.endswith('food'))

# print('i am a\t\t genius')
# print('i am a\b\b genius')
# print('i am a\n\n genius')
# print('i am a\r\r genius')

# Expression = 'This is the path to my python file - c:\python_feb\new_file\read_python\think_python'
# # Expression = 'This is the path to my python file - c:\python_feb\\new_file\\read_python\\think_python'
# Expression = r'This is the path to my python file - c:\python_feb\new_file\read_python\think_python'
# print(Expression)

# my_list = ['kunle', 'joshua', 'Bottle', 45, True, ['yam', 'rice', 'semo'], 'Bottle']
# # print(my_list)
# print(my_list[4])
# print(my_list[0])
# print(my_list[-4])
# print(my_list[-2][-2])
# print(my_list[5][1])

# print(my_list[2:])
# print(my_list[4:6])
# print(my_list[6:7])
# my_list[0] = 'Mary'
# my_list[2:6]= 'fufu'
# print(my_list)

# my_list[0:3] = ['Tolu', 'Marv']
# print(my_list)

# li = []
# li.append(['Tolu', 'Marv'])
# my_list.append('wale', False)
# li.extend(['Tolu', 'Marv'])

# my_list.clear
# # del my_list
# my_list.pop()
# my_list.remove('Bottle')
# my_list.insert(0, 'Baby')
# my_list.reverse()

# print(my_list.count('Bottle'))
# print(my_list.index('Kunle'))

# num = [30, 45, 20, 3]
# print(sum(num))
# print(max(num))
# print(min(num))

# python_student = ['tolu', 'joshua', 'femi', 'mary']
# print('Welocme to class', python_student[0])

# for each in python_student:
#     print('welcome to class', each)
#     print('-------------------')
    
# Questions = [
#     '1. Who is president of nigeria?\na.)Buhari b.)BAT'
#      '2. what is the capital of france\na.)Paris b.)London'
# ]

# for each_quest in Questions:
#     print(each_quest)
#     user = input('ans: ')

# name_of_student = []
# for x in range(10):
#     name = input(f'Name {x+1}:')
#     # name_of_student.append(name)
# num4 = ['yam', 'Rice', 'Beans',True, 12]
# B = ['Koko', 'Fale']
# num4.append(B)
# print(num4)

# items = ['Spoon','knief']
# price = [1000,2000]
# for x,y in zip (items,price):
#     print(x,y)

#Tuple()
#properties of a tuple
'''
1. unchangeable/immutable
2. they can be indexed
3.allow duplicate value
4.ordered
'''

# students = ('Damilare','Richard','Maimunat','Josh',23,False,[43,45.120])
# print(students)
#tuple can't be changed unless its converted to a list
# list_students = list(students)
# list_students[1] = 'Mary'
# students = tuple(list_students)
# print(students)

#unpacking
# students = ('Damilare','Richard','Maimunat','Josh',23,False,[43,45.120])
# (student1, student2, *alls) = students
# print(alls)
# print(student1)
# print(student2)

#Funtions of tuple
# students = ('Damilare','Richard','Richard','Maimunat','Josh',23,False,[43,45.120])
# print(students.count('Richard'))
# print(students.index('Josh'))

# student = ('Mary','Lola','Ayo','Femi')
# scores = (23, 45, 95, 30)
# print(max(scores))
# index_max = scores.index(max(scores))
# print(index_max)
# print(student[index_max])

#Zip function in a tuple
# Names = ('Mary','Lola','Ayo','Femi')
# scores = (23, 45, 95, 30)
# for name in Names:
#     print(name)

# for name, score in zip(Names,scores):
#     print(f'{name} scored {score}.')
    
# questions = [('1. Who is president of nigeria?\na.)Buhari b.)BAT','b'),
#             ('2. what is the capital of france\na.)Paris b.)London','a')
#                ]
# score = 0

# for question, ans in questions:
#      print(question)
#      user = input('Answer: ').strip().lower()
#      if user == ans:
#          print('Correct')
#          score
#      else:
#         print('Wrong')


# Name_of_students = [
#     ('Wale ','paid')
#   ]

# for Name_of_student, ans in Name_of_students:
#      print(Name_of_student)
#      user = input('Answer: ').strip().lower()
#      if user == ans:
#          print('Grant Access')
#      else:
#         print('Access Declined')

#      user = input('NAME OF STUDENT: ')
# print('Tution fee: ')


# user = input('''
#              1,Student
#              2,Staff
#              3,Visitor
#              ''')
# if user == '1':
#   students = [('Wale', 'Paid')
#               ('Shola', 'paid')
#               ]
  
  
# NAME_OF_STUDENTS = [
#   ('Wale', 'paid')
#   ('Shola', 'paid')
#   ('Kunle', 'paid')
#   ('Fola', 'paid')
# ]
# print(NAME_OF_STUDENTS)
# for Name_of_student, ans in NAME_OF_STUDENTS:
#      print(Name_of_student)
#      user = input('Answer: ').strip().lower()
#      if user == ans:
#          print('Grant Access')
#      else:
#         print('Access Declined')
        
        #While loop
# user = input('USSD: ').strip()
# while user != '*312#':
#           print('Invalid code') 
#           user = input('USSD: ').strip()


# menu_list = [
#         ('Air Jordan', '#20,000'),
#         ('Nike', '#30,100'),
#         ('Puma', '#25,300'),
#         ('Dior', '#50,000'),
#         ('NB', '#42,500 ')
# ]

# order = input('''
# WELCOME TO ICM\n Here is our menu;
#  Air Jordan= #20,000
#  Nike = #30,100
#  Puma = #25,300
#  Dior = #50,000
#  NB = #42,500           
# Kindly please place your order: ''').strip().title()

# sneakers = []
# prices = []

# orders = []
# order_prices = []

# for sneak,pri in menu_list:
#     sneakers.append(sneak)
#     prices.append(pri)
    
# if order in sneakers:
#     _index = sneakers.index(order)
#     status = prices[_index]
    
#     orders.append(order)
#     order_prices.append(status)
#     print(f'{order} is {status}')


#SET {} or ()
#Properties of a set
'''
1.unchangeable/immutable
2.it can be indexed
3.it is not indexed
4.it does not allow duplicate values
# '''
# myset = {'Apple','Pineapple','Orange','cherry'}

# #Functions
# # myset.add('Pawpaw')
# # myset.update(['Yam','Rice'])
# # myset.pop()
# myset.remove()
# myset.discard()
# # print(myset)

# setA = {5, 4, 6, 7, 8, 9, 1, 3, 2, 10, 11}
# setB = {3, 2, 4, 5, 6, 13, 12}
# setC = {3, 2, 4, 5, 6}

# # print(setA.union(setB))
# # print(setA.intersection(setB))
# # setA.intersection_update(setB)
# # print(setA.difference(setB))
# # setA.difference_update(setB)
# setA.symmetric_difference_update(setB)
# # set4 = setA.symmetric_difference(setB)
# print(setA)
# # print(set4)


#Dictionary {key:value}, dict(key=value)
#Properties
# '''
# 1.it is changeable
# 2.it is ordered
# 3.Duplicate is not allowed
# '''

# car = {'Model':'Tesla', 'Year':2023}
# print(car)
# print('The model is',car['Model'])
# car ['Model'] = 'Benz'
# print(car)

# car = {
#      'Model':'Tesla',
#      'Year':2023,
#      'Color':'Black',
#      'Year1':2024,
#      'Owner':{
#              'Name':'Dami',
#              'Price':543432
# #      }
# }

# questions = {
#         '1. Who is president of nigeria?\na.)Buhari b.)BAT':'b',
#         '2. what is the capital of france\na.)Paris b.)London':'a'
# }

# for question, ans in questions.items():
#      print(question)
#      user = input('Answer: ').strip().lower()
#      if user == ans:
#          print('Correct')
#      else:
#         print('Wrong')


# #parametrized function
# def addition (value1, value2=10):
#      result = value1 + value2
#      print(f'ans: {result}')
     
# addition(4,5)
     
 #parametrized function
 #using a global variable
 
 
# name = input('Name: ')

# def landing_page():
#     global value1
#     global value2
     
#     value1 = float(input('value1: '))
#     value2 = float(input('value2: '))

#     user = input(f'''
#             My Alata calculator.\n Welcome {name}
            
#             1. Addition
#             2. Subtraction
#             3. Multiplication
#             #. Exit
            
            
#      choose your operation:
                  
                  
#                   ''').strip()
       
#     if user == '1':
#           addition()
#     elif user == '2':
#           subtraction()
#     elif user == '3':
#           multiplication()
#     elif user == '#':
#           exit()
#     else:
#           print('Invalid Input')
#           landing_page() #recursive function
          
          
# def addition():
#      print(f'Ans: {value1+value2}')
#      mark()
   
# def subtraction():
#      print(f'Ans: {value1-value2}')
#      mark()
     
# def multiplication():
#      print(f'Ans: {value1*value2}')
#      mark()


# def mark():
#      user=input('press 1 to go home or # to exit: ').strip()
#      if user =='1':
#          landing_page()
#      else:
#           exit()     
          
# landing_page()
          
          
 #OOP
# class Dust:
#      def __init__(self):
#           first_name = ''
#           last_name = ''
#           Age = ''
              
     
#      def naming(self):
#           print('My name')
          

# Father = Dust()
          
          
          
          
          
# def add(val1: float, val2: float = 10):
#      '''
#      1. add things up
#      '''
#      return val1 + val2

# def arithmetic():
#      res = 2**add(10)
#      print(res)
     
# arithmetic()

# def add(val1: float, val2: float = 10):
#      '''
#      1. add things up
#      '''
#      return val1 + val2

# def arithmetic():
#      res = 2**add(10)
#      return res

# def printf(name):
#      print(f'{name}, your result is {arithmetic()}')
     
# printf(input('your name: '))



# Candidate = input('Matric No: ')

# def opening_page():
      
#     user = input('''
#        First Semester Mid-Semester Exam
#            1. MTH101
#            2. CHM101
#            3. PHY101453
#            #. Exit        
                   
#       Choose Your Operation:        
#                    ''').strip()
#     if user == '1':
#           MTH101()
#     elif user == '2':
#           CHM101()
#     elif user == '3':
#           PHY101()
#     elif user == '#':
#           exit()
#     else:
#           print('Invalid Input')
#           opening_page()
          
          
# def MTH101():
#       questions = {
#          'Q.1: What is the sum of 130+125+191?\nA.)335 B.)456 C.)446 D.)426':'C',
#          'Q.2: If we minus 712 from 1500, how much do we get?\nA.)788 B.)778 C.)768 D.)758':'A',
#          'Q.3: 20+(90÷2) is equal to?\nA.)50 B.)55 C.)65 D.)60':'C'
#                   }
      
#       for question, ans in questions.items():
#             print(question)
#             user = input('Answer: ').strip().upper()
#             if user == ans:
#                   print('Correct')
#             else:
#              print('Wrong')
#       mark()
             
             
# def CHM101():
#       questions = {
#             'Q1: The S.I unit of temperature is?\nA.)Fahrenheit B.)Celsius C.)Kelvin':'C',
#             'Q2: The most electronegative of the following elements is?\nA.)bromine B.)fluorine C)oxygen':'B'
#       }
    
#       for question, ans in questions.items():
#             print(question)
#             user = input('Answer: ').strip().upper()
#             if user == ans:
#                   print('Correct')
#             else:
#              print('Wrong')
#       mark()
             
             
# def PHY101():
#       questions = {
#             'Q1: The SI unit of displacement is?\nA.)Kilometer B.)Centimeter C.)Meter D.)Multimeters':'C',
#             'Q2: what is the formula for workdone?\nA.)Mass*Force B.)Force*distance C.)Acceleration/Force':'B'
#       }
      
#       for question, ans in questions.items():
#             print(question)
#             user = input('Answer: ').strip().upper()
#             if user == ans:
#                   print('Correct')
#             else:
#              print('Wrong')
# def mark():
#      user=input('press 1 to go home or # to exit: ').strip()
#      if user =='1':
#          opening_page()
#      else:
#           exit()     
          
# opening_page()


# student_DB = [
#       ('wale','male'),
#       ('funke','female')
# ]

# hello = input('your name: ').strip().lower()

# name = []
# gender = []

# for nam,gen in student_DB:
#       name.append(nam)
#       gender.append(gen)
      
#       _index = name.index(hello)
#       status = gender[_index]
      
# if hello in name:
#       print(status)




# # bucket = list()
# class Calculator:
#    def __init__(self):
#       self.calc_name = 'casio'
      
#       self.home()
      
#    def home(self):
#          print(f'Welcome to {self.calc_name}')
#          self.value1 = float(input('First value: '))
#          self.value2 = float(input('second value: '))
         
#          user = input('''
#                       1. Addition
#                       2. subtraction
#                       #. Exit
                      
#                       option: ''')
#          if user == '1':
#                self.addition()
#          elif user == '2':
#                self.subtraction()
#          elif user == '#':
#                exit()
               
#    def addition(self):
#        print(f'Ans:{self.value1 + self.value2}')
#        self.decide()
         
#    def subtraction(self):
#        print(f'Ans:{self.value1 - self.value2}')
#        self.decide()
         
#    def decide(self):
#        user = input('press 1 to go home or # to exit: ')
#        if user == '1':
#            self.home()
#        else:
#            exit()

# casio = Calculator()



# INHERITANCE

# class Parent:
#       def __init__(self) -> None:
#           self.surname = 'Ojo'
#           self.firstname = 'Mary'
#           self.hobby = 'Eating'
          
#           self.describe()
          
#       def describe(self):
#           print(f'My name is {self.firstname} {self.surname}, i love {self.hobby}')
            
# parent = Parent()


# class Child(Parent):
#     def __init__(self) -> None: 
#          super().__init__()
#          self.surname = 'Ojo'
#          self.hobby = 'Dancing'
#          self.bestfood = 'Fufu and Egusi'

#         #  self.describe()
#          self.cooking()
         
#     def cooking(self):
#         print(f'{self.surname} is cooking {self.bestfood}')
        
# child = Child()


# class Grandchild(Child):
#         def __init__(self) -> None:
#              super().__init__()
#              self.surname = 'Olawale'
#              self.action = 'Killed'
#              self.animal = 'Snake'
             
#              self.ride()
             
#         def ride(self):
#             print(f'{self.surname} {self.action} the {self.animal}')
            
# grandchild = Grandchild()


class CBT_EXAM:
  def __init__(self) -> None:
      self.CBT_name = 'cbt'  
      
      self.name()    
      
  def name(self):
      
      user = input('''
        Rain Mid-Semester Exam
           1. MTH101
           2. CHM101
           3. PHY101
           #. Exit        
                   
      Choose Your Operation:        
                   ''').strip()
      
      if user == '1':
          self.mth101()
      elif user == '2':
          self.chm101()
      elif user == '3':
          self.phy101()
      elif user == '#':
          exit()
      else:
          print('Invalid Input')
         
  def mth101(self):
      questions = {
         'Q.1: What is the sum of 130+125+191?\nA.)335 B.)456 C.)446 D.)426':'C',
         'Q.2: If we minus 712 from 1500, how much do we get?\nA.)788 B.)778 C.)768 D.)758':'A',
         'Q.3: 20+(90÷2) is equal to?\nA.)50 B.)55 C.)65 D.)60':'C'
                  }
      
      for question, ans in questions.items():
            print(question)
            user = input('Answer: ').strip().upper()
            if user == ans:
                  print('Correct')
            else:
             print('Wrong')
             self.mark()
             
             
  def chm101(self):
      questions = {
            'Q1: The S.I unit of temperature is?\nA.)Fahrenheit B.)Celsius C.)Kelvin':'C',
            'Q2: The most electronegative of the following elements is?\nA.)bromine B.)fluorine C)oxygen':'B'
      }
    
      for question, ans in questions.items():
            print(question)
            user = input('Answer: ').strip().upper()
            if user == ans:
                  print('Correct')
            else:
             print('Wrong')
             self.mark()
             
             
  def phy101(self):
      questions = {
            'Q1: The SI unit of displacement is?\nA.)Kilometer B.)Centimeter C.)Meter D.)Multimeters':'C',
            'Q2: what is the formula for workdone?\nA.)Mass*Force B.)Force*distance C.)Acceleration/Force':'B'
      }
      
      for question, ans in questions.items():
            print(question)
            user = input('Answer: ').strip().upper()
            if user == ans:
                  print('Correct')
            else:
             print('Wrong')
             self.mark()
             
  def mark(self):
     user = input('press 1 to go home or # to exit: ').strip()
     if user =='1':
         self.name()
     else:
          exit()  
          
          
cbt = CBT_EXAM()























# import datetime as dt

# tim = dt.datetime.now()
# print(tim.time())
# print(tim.date())


# import random

# # account_no = random.randint(2100000000,2199999999)
# # print(account_no)

# random.choice
# print(random.choice(['Mary', 'Kunle', 'Wale']))

# import pwinput

# password = pwinput.pwinput()
# print(password)