# Password-picker-Python
A password picker is an application that allows you to create strong passwords by combining words, numbers, and special characters.

A password prevents others from accessing our system’s e-mails and other login information. In this program, we are creating a password picker with Python to create safe and easy-to-remember passwords that will help your information to be kept private and secure.
It will create a new password and show it to you every time you run your program which is the main logic behind creating a password picker with Python.Our program keep creating a new password again and again until you find a strong and easy to remember.

A password picker randomly selects each of the four criteria i.e. adjective, name, number, special character and puts them together to create a strong password and display it on the screen. In the process, if you want another password, the program will repeat the steps, and if you no longer need a new password, the program will end.

Now let's see how to create a password picker with Python using the random module in Python. Our program should use random choices from the group of adjectives, nouns, numbers, and special characters.
first we need to create a list of adjectives and nouns and pick a random word from each list. For that we need to import random module in beginning of code and use the choice function in the random module. Then we have to use the randrange() function in the random module to select a random number between 0 and 99 and use the choice function again to pick a random punctuation mark from string module. Finally we have to combine everything to create a new password and our appliaction is ready.
