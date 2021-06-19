# automated-personal-dictionary

A useful automated application written in Python that retrieves and previews the definition of a selected word for you, as well as assisting in the creation of a personal dictionary, all with the click of a button.

# Use Case

<p>When we read something in a pdf, on the internet, or on our desktop, we frequently get stuck on a word that is unfamiliar or new to us, and we may want to write it down with its definition for future reference. This python application could be useful in this situation. By simply pressing a button, it will take care of noting down the word and its definition.</p>
<p>Whenever this python script is running, all you have to do is copy the word you want to remember and then hit <b>ctrl + I</b> This will cause it to search the internet (vocabulary.com in this case) for the definition of that specific word and save it in a file for future reference. Once started, this script will execute till you press <b>ctrl + e</b>.  </p>

# Technical details
This python script (**dictionary.py**) uses the build in tkinter module to get the copied word from the Windows clipboard. To get the definition from vocabulary.com, BeautifulSoup is utilised as a web scrapper. The requests are handled by the Requests module. To look up the definition, it will require an active internet connection. It will produce two files, one containing all of the definitions and the other containing a list of all of the words that have previously been saved in order to avoid duplicate entries. It will also generate a new session each time the application is launched to keep track of the time and date when the definitions were written. Aside from that, few things can be modified as per your requirement like You can disable session creation as needed, alter the hotkeys **ctrl + I** and **ctrl + E** if they're used for something else, and alter the name of the file where the definitions are saved. It may occasionally produce erroneous results, but this is quite unusual.

# Snapshot 

( **Created Dictionary** )
![image](https://user-images.githubusercontent.com/31349598/122264106-ca852e80-cef4-11eb-9772-888c964fb2fd.png)

( **Created word list** )
![image](https://user-images.githubusercontent.com/31349598/122264371-17690500-cef5-11eb-92f4-3858c16a3254.png)

# Updates
The definition of the selected word will now appear in the notification when you hit ctrl + c, and it will only be added to the dictionary if you press ctrl + i.

<img width="286" alt="Notification" src="https://user-images.githubusercontent.com/31349598/122639403-46f75780-d117-11eb-8ca7-5e695731d49a.png"> 
