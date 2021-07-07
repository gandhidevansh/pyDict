from bs4 import BeautifulSoup
import requests
from datetime import datetime
import keyboard
import time
from tkinter import Tk
from win10toast import ToastNotifier

fileHandler = open('dictionary.txt', 'a')
listHandler = open('list.txt', 'a')
session = 0
toast = ToastNotifier()

while True:
    
    if keyboard.is_pressed('ctrl + c'):
        time.sleep(1)
        word = Tk().clipboard_get()
        
        try:
            URL = "https://www.vocabulary.com/dictionary/" + word
            page = requests.get(URL)
                    
            content = BeautifulSoup(page.content, 'html.parser')
            results = content.find(class_='definition')
            definition = ' '.join(results.text.split()[1:])
            toast.show_toast(word, definition, duration=5, icon_path = "Dic.ico", threaded=True)
        
        except AttributeError:
            toast.show_toast("Error", "Please a single word", duration=5, icon_path = "Dic.ico", threaded=True)
        

    elif keyboard.is_pressed('ctrl + i'):

        if (session == 0):
            fileHandler.write('-'*35 + 'New Session' + '(' + str(datetime.now()) + ')' + '-'*35 + '\n')
            session = 1
            
        flag = 0
    
        listHandler = open('list.txt', 'r')
        for w in listHandler:
            if word in w:
                toast.show_toast(word, "Already added to the dictionary", duration=5, icon_path = "Dic.ico", threaded=True)
                flag = 1
                break

        if (flag == 0):
            toast.show_toast(word, "Added to the dictionary!✌", duration=5, icon_path = "Dic.ico", threaded=True)
            fileHandler.write('#' + word.upper() + '\n')
            fileHandler.write(definition.lower() + '\n' + '\n')
            
            listHandler = open('list.txt', 'a')
            listHandler.write(word + '\n')
            listHandler.close()

    elif keyboard.is_pressed('ctrl + e'):
        break

fileHandler.close()
