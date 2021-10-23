import random, datetime, calendar, sys, time
from datetime import date

 
time_now = datetime.datetime.now().hour
 
 
today_date = date.today()
calendar.day_name[today_date.weekday()]
 

if time_now < 12:
   user_name = input('Good morning, stranger. I am Studybot. What is your name? ')
   print(f'Hello, {user_name}. Happy {calendar.day_name[today_date.weekday()]}! ') 
   study_ans = str.lower(input('Ready to study? '))
   if study_ans == 'yes':
    subject_ans = str.lower(input('What subject do you want to study today {user_name} ? '))
   else:
    print('Okay... see you next time!')
    sys.exit()


   while True:
    if subject_ans == 'anatomy':
     print('hello world')
     break
    elif subject_ans == 'chemistry':
     print('hello world 2')
     break
    elif subject_ans == 'epidemiology':
     print('hello world 3')
     break
    else:
     sec_try = str.lower(input("Sorry, I don't support that yet.. would you like to pick another subject? "))
    if sec_try == 'yes':
     subject_ans = str.lower(input(f'What subject do you want to study today {user_name} ? '))
   else:
    print('Okay... see you next time!')
    sys.exit()
   

elif time_now > 12:
   user_name = input('Good afternoon, stranger. I am Chatbot. What is your name? ')
   print(f'Hello, {user_name}. Happy {calendar.day_name[today_date.weekday()]}! ')
   study_ans = str.lower(input('Ready to study? '))
   if study_ans == 'yes':
    subject_ans = str.lower(input(f'What subject do you want to study today {user_name} ? '))
   else:
    print('Okay... see you next time!')
    sys.exit()


   while True:
    if subject_ans == 'anatomy':
     print('hello world')
     break
    elif subject_ans == 'chemistry':
     print('hello world 2')
     break
    elif subject_ans == 'epidemiology':
     print('hello world 3')
     break
    else:
     sec_try = str.lower(input("Sorry, I don't support that yet.. would you like to pick another subject? "))
    if sec_try == 'yes':
     subject_ans = str.lower(input(f'What subject do you want to study today {user_name} ? '))
   else:
    print('Okay... see you next time!')
    sys.exit()

elif time_now > 6:
   user_name = input('Good evening, stranger. I am Chatbot. What is your name? ')
   print(f'Hello, {user_name}. Happy {calendar.day_name[today_date.weekday()]}! ')
   study_ans = str.lower(input('Ready to study? '))
   if study_ans == 'yes':
    subject_ans = str.lower(input(f'What subject do you want to study today {user_name} ? '))
   else:
    print('Okay... see you next time!')
    sys.exit()


   while True:
    if subject_ans == 'anatomy':
     print('hello world')
     break
    elif subject_ans == 'chemistry':
     print('hello world 2')
     break
    elif subject_ans == 'epidemiology':
     print('hello world 3')
     break
    else:
     sec_try = str.lower(input("Sorry, I don't support that yet.. would you like to pick another subject? "))
    if sec_try == 'yes':
     subject_ans = str.lower(input(f'What subject do you want to study today {user_name} ? '))
   else:
    print('Okay... see you next time!')
    sys.exit()

