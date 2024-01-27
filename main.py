import random, os
import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


# SETTINGS#

numOfItems = 5
numOfGuesses = 5
seconds = 1
numOfCorrectGuesses = numOfItems

items = ["phone", "clothing", "toothbrush", "money", "floss", "books", "shoes", "wi-fi", "stuffies", "glasses"]

places = ["hawaii", "vietnam", "taiwan", "japan", "paris"]

myluggage = []

for i in range(numOfItems):
    packing = random.choice(items)
    # Add the variable packing into myluggage
    myluggage.append(packing)
    # Remove the variable packing from items
    items.remove(packing)

print("welcome to Not Sus Airlines. the NSA. take a seat.")
print("We are preparing your flight to " + random.choice(places))
print("quick! you have... 5 seconds to pack! hurry up!")
print(myluggage)
countdown(seconds)  # countdown
os.system('clear')  # make it disappear
guesses = 0
correctguesses = 0

while (guesses < numOfGuesses):
    # take an input from the user and ask them for an item that they saw
    i = input("what items were there? ")
    if i in myluggage:
        # print a message saying yes this item is in our luggage
        print("yes, this item is in our luggage.")
        # add one onto guesses and correct guesses
        guesses += 1
        correctguesses += 1

    else:
        print("c'mon man! this is ez. how did you not get this right?")
        guesses += 1

    # if correct_guesses equals to 3, print out they won and they can now travel
    if (correctguesses == numOfCorrectGuesses):
        print("good, i guess.")
        break

# if their correct_guesses is less than 3, print out they cannot board
if (correctguesses < numOfCorrectGuesses):
    print("wooohooo! you loooossssttttt!!!! uhhhh... i mean.... im sorry. you cant board.")



