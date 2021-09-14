import random



def bot_reply(user_input):
  responses = []
  with open('responses.txt', 'r') as f:
   responses = f.read().split()
 
  return random.choice(responses)

def init_chat():
  quit_code = 'bye'

  user_input = input('Hello, I am Chatbot. How are you? ')

  while user_input != quit_code:

    user_input = input(bot_reply(user_input) + "\n")


if __name__ == "__main__":
  init_chat()