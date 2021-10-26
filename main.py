import datetime, calendar, sys, random, time
from datetime import date
from pytz import timezone

zone = 'CST6CDT'
 
time_now = datetime.datetime.now(timezone(zone)).hour
 
 
today_date = date.today()
calendar.day_name[today_date.weekday()]
 
questionsa = ['anatomy1', 'anatomy2', 'anatomy3']
questionsb = ['chem1', 'chem2', 'chem3']
questionsc = ['ep1', 'ep2', 'ep3']



if time_now < 12:
   user_name = input('Good morning, stranger. I am Studybot. What is your name? ')
   print(f'Hello, {user_name}. Happy {calendar.day_name[today_date.weekday()]}! ') 
   study_ans = str.lower(input('Ready to study? '))
   if study_ans == 'yes':
    subject_ans = str.lower(input(f'What subject do you want to study today {user_name} ? '))
   else:
    print('Okay... see you next time!')
    sys.exit()

# running questions for anatomy

   while True:
    if subject_ans == 'anatomy':
     print('loading questions...')
     print("Once you're done, input 'quit' instead of an answer.")
     time.sleep(1)
     keep_running = True
     while keep_running:
      this = random.choice(questionsa)
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

     # running questions for chem

    elif subject_ans == 'chemistry':
     print('loading questions...')
     time.sleep(1)
     keep_running = True
     while keep_running:
       chem_q = random.choice(questionsb)
       if chem_q == 'chem1':
         chem_ans = str.lower(input('Is dissolving a physical or a chemical change? '))
         if chem_ans == 'quit':
           print('Bye, see you next time!')
           sys.exit()
         elif 'physical' not in chem_ans:
           print('Not quite...')
         else:
            print('Correct!')
       elif chem_q == 'chem2':
         chemtwo_ans = str.lower(input('Does oxidation cause an atom to lose or gain electrons? '))
         if chemtwo_ans == 'quit':
           print('Bye bye!')
           sys.exit()
         elif 'lose' not in chemtwo_ans:
           print('Nope...')
         else:
           print('You got it!')
       elif chem_q == 'chem3':
         chemthr_ans = str.lower(input('Does reduction cause an atom to lose or gain electrons? '))
         if chemthr_ans == 'quit':
           print('See you!')
           sys.exit()
         elif 'gain' not in chemthr_ans:
           print('Incorrect...')
         else:
           print('Correct!')      
     break
     #running questions for disease

    elif subject_ans == 'epidemiology':
     print('loading questions...')
     time.sleep(1)
     keep_running = True
     while keep_running:
       ep_q = random.choice(questionsc)
       if ep_q == 'ep1':
         ep_ans = str.lower(input('What is a sudden increase in the number of cases in an area called? '))
         if ep_ans == 'quit':
           ('Bye!')
           sys.exit()
         elif 'epidemic' not in ep_ans:
           print('Incorrect...')
         else:
           print('Thats right!')
       elif ep_q == 'ep2':
          epidemics = ['Yellow fever', 'Measles', 'Covid-19','Polio' ]
          print(*epidemics, sep = '\n')
          eptwo_ans = str.lower(input('Which one is NOT an epidemic? '))
          if eptwo_ans == 'quit':
            ('See you later!')
          elif 'covid-19' not in eptwo_ans:
            print('Nope!')
          else: 
            print('Thats correct!')
       elif ep_q == 'ep3':
          epthr_ans = str.lower(input('What are organisms that can transmit infectious pathogens between humans called? '))
          if epthr_ans == 'quit':
            ('Bye!')
          elif 'vectors' not in epthr_ans:
            print('Not quite!')
          else:
            print('Correct!')
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

# running questions for anatomy 
   while True:
    if subject_ans == 'anatomy':
     print('loading questions...')
     time.sleep(1)
     keep_running = True
     while keep_running:
      this = random.choice(questionsa)
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

        #running questions for chem

    elif subject_ans == 'chemistry':
     print('loading questions...')
     time.sleep(1)
     keep_running = True
     while keep_running:
       chem_q = random.choice(questionsb)
       if chem_q == 'chem1':
         chem_ans = str.lower(input('Is dissolving a physical or a chemical change? '))
         if chem_ans == 'quit':
           print('Bye, see you next time!')
           sys.exit()
         elif 'physical' not in chem_ans:
           print('Not quite...')
         else:
            print('Correct!')
       elif chem_q == 'chem2':
         chemtwo_ans = str.lower(input('Does oxidation cause an atom to lose or gain electrons? '))
         if chemtwo_ans == 'quit':
           print('Bye bye!')
           sys.exit()
         elif 'lose' not in chemtwo_ans:
           print('Nope...')
         else:
           print('You got it!')
       elif chem_q == 'chem3':
         chemthr_ans = str.lower(input('Does reduction cause an atom to lose or gain electrons? '))
         if chemthr_ans == 'quit':
           print('See you!')
           sys.exit()
         elif 'gain' not in chemthr_ans:
           print('Incorrect...')
         else:
           print('Correct!') 
     break

     # running questions for disease

    elif subject_ans == 'epidemiology':
     print('loading questions...')
     time.sleep(1)
     keep_running = True
     while keep_running:
       ep_q = random.choice(questionsc)
       if ep_q == 'ep1':
         ep_ans = str.lower(input('What is a sudden increase in the number of cases in an area called? '))
         if ep_ans == 'quit':
           ('Bye!')
           sys.exit()
         elif 'epidemic' not in ep_ans:
           print('Incorrect...')
         else:
           print('Thats right!')
       elif ep_q == 'ep2':
          epidemics = ['Yellow fever', 'Measles', 'Covid-19','Polio' ]
          print(*epidemics, sep = '\n')
          eptwo_ans = str.lower(input('Which one is NOT an epidemic? '))
          if eptwo_ans == 'quit':
            ('See you later!')
          elif 'covid-19' not in eptwo_ans:
            print('Nope!')
          else: 
            print('Thats correct!')
       elif ep_q == 'ep3':
          epthr_ans = str.lower(input('What are organisms that can transmit infectious pathogens between humans called? '))
          if epthr_ans == 'quit':
            ('Bye!')
          elif 'vectors' not in epthr_ans:
            print('Not quite!')
          else:
            print('Correct!')
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

# running questions for anatomy

   while True:
    if subject_ans == 'anatomy':
     print('loading questions...')
     time.sleep(1)
     keep_running = True
     while keep_running:
      this = random.choice(questionsa)
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

     #running questions for chem

    elif subject_ans == 'chemistry':
     print('loading questions...')
     time.sleep(1)
     keep_running = True
     while keep_running:
       chem_q = random.choice(questionsb)
       if chem_q == 'chem1':
         chem_ans = str.lower(input('Is dissolving a physical or a chemical change? '))
         if chem_ans == 'quit':
           print('Bye, see you next time!')
           sys.exit()
         elif 'physical' not in chem_ans:
           print('Not quite...')
         else:
            print('Correct!')
       elif chem_q == 'chem2':
         chemtwo_ans = str.lower(input('Does oxidation cause an atom to lose or gain electrons? '))
         if chemtwo_ans == 'quit':
           print('Bye bye!')
           sys.exit()
         elif 'lose' not in chemtwo_ans:
           print('Nope...')
         else:
           print('You got it!')
       elif chem_q == 'chem3':
         chemthr_ans = str.lower(input('Does reduction cause an atom to lose or gain electrons? '))
         if chemthr_ans == 'quit':
           print('See you!')
           sys.exit()
         elif 'gain' not in chemthr_ans:
           print('Incorrect...')
         else:
           print('Correct!') 
     break

     #running questions for disease

    elif subject_ans == 'epidemiology':
     print('loading questions...')
     time.sleep(1)
     keep_running = True
     while keep_running:
       ep_q = random.choice(questionsc)
       if ep_q == 'ep1':
         ep_ans = str.lower(input('What is a sudden increase in the number of cases in an area called? '))
         if ep_ans == 'quit':
           ('Bye!')
           sys.exit()
         elif 'epidemic' not in ep_ans:
           print('Incorrect...')
         else:
           print('Thats right!')
       elif ep_q == 'ep2':
          epidemics = ['Yellow fever', 'Measles', 'Covid-19','Polio' ]
          print(*epidemics, sep = '\n')
          eptwo_ans = str.lower(input('Which one is NOT an epidemic? '))
          if eptwo_ans == 'quit':
            ('See you later!')
          elif 'covid-19' not in eptwo_ans:
            print('Nope!')
          else: 
            print('Thats correct!')
       elif ep_q == 'ep3':
          epthr_ans = str.lower(input('What are organisms that can transmit infectious pathogens between humans called? '))
          if epthr_ans == 'quit':
            ('Bye!')
          elif 'vectors' not in epthr_ans:
            print('Not quite!')
          else:
            print('Correct!')
     break
     
    else:
     sec_try = str.lower(input("Sorry, I don't support that yet.. would you like to pick another subject? "))
    if sec_try == 'yes':
     subject_ans = str.lower(input(f'What subject do you want to study today {user_name} ? '))
   else:
    print('Okay... see you next time!')
    sys.exit()

