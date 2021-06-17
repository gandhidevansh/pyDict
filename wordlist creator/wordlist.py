import keyboard
from tkinter import Tk

listHandler = open('wordlist.txt', 'a')

while True:
    if keyboard.is_pressed('ctrl + i'):
        flag = 0
            
        listHandler = open('wordlist.txt', 'r')
        for w in listHandler:
            if word in w:
                flag = 1
                break

        if (flag == 0):
            listHandler = open('wordlist.txt', 'a')
            listHandler.write(word + '\n')
            listHandler.close()
                
            print(word + ' ' + 'added succesfully...')

    elif keyboard.is_pressed('ctrl + c'):
        word = Tk().clipboard_get()

    elif keyboard.is_pressed('ctrl + e'):
        break
