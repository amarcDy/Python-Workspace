import sys
from datetime import datetime

#Gets the name of the user
user_name:str= input('Hello there I\'m Chatbot! What is your name?')
print(f'Nice to meet you {user_name}!')


def get_response(text:str) ->str:
    lowered: str=text.lower()
    if lowered in ['hello','hi','hey']:
        return f'Hey there {user_name}! How are you?'
    elif lowered in ['how are you?']:
        return 'I\'m doing great! What about you?'
    elif lowered in ['time']:
        current_time = datetime.now()
        return f'Currently it is {current_time.strftime("%H:%M %S")}'
    elif lowered in ['bye','see you','goodbye']:
        return 'It\'s been a pleasure talking to you! Bye!'
    elif lowered in ['you?','your name']:
        return 'I am ChatBot, nice to meet you!'
    else:
        return f'Sorry, I do not understand "{text}"'



while True:
    user_input = input(f'{user_name}: ')
    if user_input == 'exit':
        print ('Goodbye!')
        sys.exit()

    bot_response =  get_response(user_input)
    print (f'Chatbot: {bot_response}')
