import keyboard
from tkinter import Tk

noteHandler = open('notes.txt', 'a')

noteHandler.write('#'*80 + '\n')
num = 1

while True:
    if keyboard.is_pressed('ctrl + i'):
        flag = 0
            
        noteHandler = open('notes.txt', 'r')
        for w in noteHandler:
            if word in w:
                flag = 1
                break

        if (flag == 0):
            noteHandler = open('notes.txt', 'a')
            noteHandler.write(str(num) + ') ' + word + '\n' + '\n')
            noteHandler.close()
            num = num +1

    elif keyboard.is_pressed('ctrl + c'):
        word = Tk().clipboard_get()

    elif keyboard.is_pressed('ctrl + e'):
        break
