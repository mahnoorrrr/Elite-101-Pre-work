option_list = ['1. I feel bad about my work, am I doing good?', 
               '2. I made a mistake, what should I do?', 
               '3. Does anyone truly love me for who I am?', 
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
 #Implement option responses
 if helping_the_user == '1':
   print('Your work is SO good! You must not doubt yourself.')
   print(f'I believe in you {name} and in your work and competence even more!')
 elif helping_the_user == '2': 
   print('I make mstks all the time!')
   print(f'And you\'re only {age} years old,')
   print('No matter how old one is they still make mistkes.')
   print('If you made a mistake in your work, maybe ask someone else for help')
   print('And if your mistake was in your love life, tell them you\'ll fix it NOW!')
   print('And if it was a mistake so big you can\'t fix it, life always gets better:)')
 elif helping_the_user == '3':
   print('I truly love you for you!!!')
   print('...and I am always here for you...always')
 #add exit option
 elif helping_the_user == '4':
   print(':( it\'s so sad to see you go, but I love watching you leave')
   print('I\'LL STAY HERE FOREVER...WAITING FOR YOU')

#running code from here:
chat_bot()