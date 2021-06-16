# automated-personal-dictionary

A handy automated tool made using python that helps to create a personal dictionary just by pressing a button. 

# Use Case

When we read something in a pdf, on the internet, or on our desktop, we frequently get stuck on a word that is unfamiliar or new to us, and we may want to write it down with its definition for future reference. This python application could be useful in this situation. By simply pressing a button, it will take care of noting down the word and its definition.
Whenever this python script is running, all you have to do is copy the word you want to remember and then hit **ctrl + I** This will cause it to search the internet (vocabulary.com in this case) for the definition of that specific word and save it in a file for future reference. Once started, this script will execute till you press **ctrl + e**. 

# Technical details
This python script uses the win32clipboard module to get the copied word from the Windows clipboard. To get the definition from vocabulary.com, BeautifulSoup is utilised as a web scrapper. The requests are handled by the Requests module. To look up the definition, it will require an active internet connection. It will produce two files, one containing all of the definitions and the other containing a list of all of the words that have previously been saved in order to avoid duplicate entries. It will also generate a new session each time the application is launched to keep track of the time and date when the definitions were written. Aside from that, few things can be modified as per your requirement like You can disable session creation as needed, alter the hotkeys ctrl + I and ctrl + E if they're used for something else, and alter the name of the file where the definitions are saved.
