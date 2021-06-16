from bs4 import BeautifulSoup
import requests
from datetime import datetime
import keyboard
from tkinter import Tk

fileHandler = open('dictionary.txt', 'a')
listHandler = open('list.txt', 'a')

fileHandler.write('-'*35 + 'New Session' + '(' + str(datetime.now()) + ')' + '-'*35 + '\n')

while True:
    if keyboard.is_pressed('ctrl + i'):
        flag = 0
        
        try:
            
            listHandler = open('list.txt', 'r')
            for w in listHandler:
                if word in w:
                    flag = 1
                    break

            if (flag == 0):

                URL = "https://www.vocabulary.com/dictionary/" + word
                page = requests.get(URL)
                    
                content = BeautifulSoup(page.content, 'html.parser')
                results = content.find(class_='definition')
                definition = ' '.join(results.text.split()[1:])
                fileHandler.write('#' + word.upper() + '\n')
                fileHandler.write(definition.lower() + '\n' + '\n')

                listHandler = open('list.txt', 'a')
                listHandler.write(word + '\n')
                listHandler.close()
                
                print(word + ' ' + 'added succesfully...')
        
        except AttributeError:
            print("Please select a single word!")

    elif keyboard.is_pressed('ctrl + c'):
        word = Tk().clipboard_get()

    elif keyboard.is_pressed('ctrl + e'):
        break

fileHandler.close()
