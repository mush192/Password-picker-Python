import random
import string
print("Welcome to Password Picker")

adjectives = ['Sleepy', 'Slow', 'Smelly', 'Wet', 'Fat', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Fluffy', 'White', 'Proud', 'Brave','Adorable','Adventurous','Aggressive','Agreeable','Alert','Alive']
nouns = ['Apple', 'Dinosaur', 'Ball', 'Toaster', 'Goat', 'Dragon', 'Hammer', 'Duck', 'Panda','Ability','Access','Accident','Account','Act','Action','Back','Bad','Balance','Bank','Baseball','Basis','Basket']

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print("You Password is : %s" % password)

    response = input("Would you like another password? Type Y or N: ")
    if response == 'N':
        break 