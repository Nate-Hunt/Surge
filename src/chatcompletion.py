import os
import openai

from dotenv import load_dotenv

load_dotenv()

def chat_bot_temp(key):
    openai.api_key = key

    print("************************************************************************************************************\n")
    chat_input = input("Hey there, what did you want to ask? \n")

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": chat_input}])
    print("\nYou can stop stop the conversation by saying 'Stop'.")
    print(chat_completion.choices[0].message.content)

    while chat_input:
        chat_input = input()
        if(chat_input != 'Stop' and chat_input != 'stop'):
            chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": chat_input}])
            print("\n", chat_completion.choices[0].message.content, "\n")
        else: break

    print("************************************************************************************************************")
    
    
def chat_bot(message):
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}])
    return chat_completion.choices[0].message.content