option_list = ['1. I feel bad about my work, am I doing good?', \
               '2. I made a mistake, what should I do?', \
               '3. Does anyone truly love me for who I am?', \
               '4. I want to exit the chatbot space']
def chat_bot():
 #welcome message
 print('Welcome to my space, it\'s nice to meet you! My name is Chatbot.')
 #collect user name+age
 name = input('What\'s your name?')
 age = input(f'You look so young {name}, how old are you?')
 #ask user how chatbot can assist them
 for option in option_list: 
  print(option)
 helping_the_user = input('OK bestie, chose the option you want to talk about:')
 #Implement options as well as the responses
 #if helping_the_user == '1':
 #add exit option


#running code from here:
chat_bot()