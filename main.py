import datetime, calendar, sys, random, time
from datetime import date

 
time_now = datetime.datetime.now().hour
 
 
today_date = date.today()
calendar.day_name[today_date.weekday()]
 
questions = ['anatomy1', 'anatomy2', 'anatomy3']
random.shuffle(questions)

if time_now < 12:
   user_name = input('Good morning, stranger. I am Studybot. What is your name? ')
   print(f'Hello, {user_name}. Happy {calendar.day_name[today_date.weekday()]}! ') 
   study_ans = str.lower(input('Ready to study? '))
   if study_ans == 'yes':
    subject_ans = str.lower(input(f'What subject do you want to study today {user_name} ? '))
   else:
    print('Okay... see you next time!')
    sys.exit()


   while True:
    if subject_ans == 'anatomy':
     print('loading questions...')
     keep_running = True
     while keep_running:
      this = random.choice(questions)
      if this == 'anatomy1':
       ans_input = str.lower(input('What is the most basic cell in the nervous system? '))
       if ans_input == 'quit': 
        print('Bye!')
        sys.exit()
       elif 'neuron' not in ans_input:
        print('Wrong...')
       else: 
        print('Correct!')
      elif this == 'anatomy2':
       anstwo_input = str.lower(input('What do neurons do? '))
       if anstwo_input == 'quit':
        print('See you later!')
        sys.exit()
       elif 'transmit impulses' not in anstwo_input:
        print('Incorrect...')
       else:
        print('Yes!')
      elif this == 'anatomy3':
       ansthr_input = str.lower(input('What is the central nervous system made up of? '))
       if ansthr_input == 'quit':
        print('Goodbye!')
        sys.exit()
       elif 'brain and spinal cord' not in ansthr_input:
        print('Not quite...')
       else:
        print('Good job!')
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
     keep_running = True
     while keep_running:
      this = random.choice(questions)
      if this == 'anatomy1':
       ans_input = str.lower(input('What is the most basic cell in the nervous system? '))
       if ans_input == 'quit': 
        print('Bye!')
        sys.exit()
       elif 'neuron' not in ans_input:
        print('Wrong...')
       else: 
        print('Correct!')
      elif this == 'anatomy2':
       anstwo_input = str.lower(input('What do neurons do? '))
       if anstwo_input == 'quit':
        print('See you later!')
        sys.exit()
       elif 'transmit impulses' not in anstwo_input:
        print('Incorrect...')
       else:
        print('Yes!')
      elif this == 'anatomy3':
       ansthr_input = str.lower(input('What is the central nervous system made up of? '))
       if ansthr_input == 'quit':
        print('Goodbye!')
        sys.exit()
       elif 'brain and spinal cord' not in ansthr_input:
        print('Not quite...')
       else:
        print('Good job!')
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
     print('loading questions...')
     time.sleep(2)
     keep_running = True
     while keep_running:
      this = random.choice(questions)
      if this == 'anatomy1':
       ans_input = str.lower(input('What is the most basic cell in the nervous system? '))
       if ans_input == 'quit': 
        print('Bye!')
        sys.exit()
       elif 'neuron' not in ans_input:
        print('Wrong...')
       else: 
        print('Correct!')
      elif this == 'anatomy2':
       anstwo_input = str.lower(input('What do neurons do? '))
       if anstwo_input == 'quit':
        print('See you later!')
        sys.exit()
       elif 'transmit impulses' not in anstwo_input:
        print('Incorrect...')
       else:
        print('Yes!')
      elif this == 'anatomy3':
       ansthr_input = str.lower(input('What is the central nervous system made up of? '))
       if ansthr_input == 'quit':
        print('Goodbye!')
        sys.exit()
       elif 'brain and spinal cord' not in ansthr_input:
        print('Not quite...')
       else:
        print('Good job!')
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

