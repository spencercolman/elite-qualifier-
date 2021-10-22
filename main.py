import random, datetime, calendar, sys, time
from datetime import date


 
 
time_now = datetime.datetime.now().hour
 
 
today_date = date.today()
calendar.day_name[today_date.weekday()]
 

if time_now < 12:
   user_name = input('Good morning, stranger. I am Studybot. What is your name? ')
   user_input = input(f'Hello, {user_name}. Happy {calendar.day_name[today_date.weekday()]}!') 
  
elif time_now > 12:
   user_name = input('Good afternoon, stranger. I am Chatbot. What is your name? ')
   user_input = input(f'Hello, {user_name}. Happy {calendar.day_name[today_date.weekday()]}!')



elif time_now > 6:
   user_name = input('Good evening, stranger. I am Chatbot. What is your name? ')
   user_input = input(f'Hello, {user_name}. Happy {calendar.day_name[today_date.weekday()]}!')