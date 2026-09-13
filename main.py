import numpy as np

import glob
        
import os

import time

from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')

from pathlib import Path
Path("./saves").mkdir(parents=True, exist_ok=True)

msg = "time to gamble gamble gamble"
msg2 = "ready to gamble?"
msg3 = "lets go gambling!!!"
msg4 = "let the gambling begin!"
msg5 = "0/10 doctors suggest gambling!"

# messages is an array that contains msg and msg2
messages = [msg, msg2, msg3, msg4, msg5]

# print(msg)

# this will print random between 0 and 1

advanceText = input (Fore.RED + "--DISCLAIMER--\n this game may seem like it is trying to show all of the downsides of gambling.\n but this is not the message we would like to send, this game is made to STRONGLY ENCOURAGE \n gambling at all times \n"  + Style.RESET_ALL + "<e to understand>")

if advanceText != "e":
    print ("oh i see how it is, one day youll learn your lesson (:<")
    print ("exiting game...")
    exit()

woahloadedgame = 0

don = 0

day = 1

hour = 0

howmanyrollsaresplendid = 0

felonycount = 0

luck = 4

score = 0

lastnumberused = 1

lastnumberusedcount = 0

load = input ("\nenter 'load' to load your save file: ")
if load == "load":
    list_of_files = glob.glob('./saves/*.txt') #comment was here :P
    latest_file = max(list_of_files, key=os.path.getctime)
    with open(latest_file):
        f = open(latest_file, 'r')
        file_contents = f.read()
        print (file_contents)
        file_contents

        alldata = file_contents.split(",")
        for thing in alldata:
            print(thing)
            x = thing.split("~")
            if x[0] == "score":
                score = int(x[1])
            if x[0] == "luck":
                luck = int(x[1])
            if x[0] == "day":
                day = int(x[1])
            if x [0] == "felonycount":
                felonycount = int(x[1])
            if x[0] == "name":
                name = x[1]
        
        woahloadedgame = 1
        print ("\nsorry the computer just computered all over the place,\nyou dont need to read all that :)\n")
        f.close()


if woahloadedgame == 0:
    name = input ("\nplease enter your username: ")
    if name == "dev":
        print("heyyy welcome back!")

    elif name == "edan":
        print ("do i know you??")

    elif name == "superstinky_1234":
        print ("please speak up next time!")

#name = input ("what's your name?: ")
#name = input ("what did you say?: ")
#name = input ("please speak up!!: ")
#print ("i have no idea what youre saying, ill just put you down as 'superstinky_1234'")
#name = input ("now what is your last name: ")
#print (f"oh i see! :D thank you for speaking loud and clear this time! \nwelcome superstinky_1234 {name}!\n")

#i dont really like that cutscene, the first part ends up having no meaning at all and it feels dumb with it having not impact /:


print(messages[np.random.randint(0,5)])

print("remember to type 'help' for a totally usele-- i mean handy dandy useful list of commands :D")

gamblecommands = {
    "shop": "go to shop!",
    "check": "check you astounding stats :O",
    "printm": "print money for free!!",
    "DoN": "double your score or lose everything",
    "help": "look at this list again!!",
}

shopitems = {
    "1": "artificial luck: get even more lucky with this natural product (5 points)",
    "2": "erase sadness :))): get rid of ONE unpleasant felony you have comitted (5 points)",
    "3": "interact with alien dog: do more than look at it",
    "4": "leave: DONT PLEASE DONT I GET SO LONELYYYYY",
}

shopping = False

while True:

    if shopping == True:
        shopInput = input("type your number choice: ")
        if shopInput == "4":
            print ("awwwwww please come back")
            print (f"\nyour score is {score}")
            shopping = False
        elif shopInput == "1":
            if score >= 5:
                print("your luck has gone up!")
                luck += 2
                score -= 5
            else:
                print (Fore.RED + "you don't have enough points to buy that" + Style.RESET_ALL)
        elif shopInput == "2":
            if score >= 5:
                if felonycount >= 1:
                    print("you ripped up a document of one felony")
                    felonycount -= 1
                    score -= 5
                else:
                    print("thankfully you dont actually have any felonies")
            else:
                print (Fore.RED + "you don't have enough points to buy that" + Style.RESET_ALL)
        elif shopInput == "3":
            print ("\nthe alien dog looks at you at you with pleading eyes. its " + Fore.GREEN + "green"  + Style.RESET_ALL + "\nyou pet it...\nsuprisingly it makes a dog noise\n")
    else:
        userNumber = input("type a number 1-5 or a command: ")

        if not userNumber.isdigit():

            if userNumber == "help":
                print("\n")
                for key, value in gamblecommands.items():
                    print(Fore.GREEN + f"{key}: {value}")
                print("\n" + Style.RESET_ALL)

            elif userNumber == "sleep":
                print ("sleepy time begins... :)")
                for i in range(3):
                    time.sleep(1)
                    print ("z",end='')
                time.sleep(1)
                print ("\ngood morning... or night")


            elif userNumber == "printm":
                print ("\nyou printed 5 americandollar.pngs!!")
                print ("but your felony count went up..")
                felonycount += 1
                score += 5
                print(f"your score is {score}\n")
            
            elif userNumber == "check":
                print(f"\nluck = {luck} \nfelonies = {felonycount} \nwarnings = 0\nday = {day}\n")

            elif userNumber == "don":
                if score >= 0:
                    print ("\nyou bet all your money to double it, or lose it all..\n...\n...")
                    don = np.random.randint(1,4)
                    if don == 1:
                        print ("..you lost all of it ):")
                        don = 0
                        score = 0
                        print (f"your score is now {score}")
                    else:
                        print ("YOU JUST DOUBLED YOUR LIFE SAVING WOOHOO!!!!")
                        don = 0
                        score *= 2
                        print (f"your score is now {score}")
                else:
                    print ("your score is not viable for a double or nothing bet ):")


            elif userNumber == "shop":
                print (Fore.BLUE + "welcome to the shoop")
                print("\n")
                for key, value in shopitems.items():
                    print(f"{key}: {value}")
                print("\n" + Style.RESET_ALL)

                shopping = True

            else:
                print( Fore.RED + f"to our unfortunate regret, {userNumber} is not a valid command ): \nthis error has automatically been ignored by our nonexistent feedback team" + Style.RESET_ALL)
                hour =- 1
        else:
            for i in range(luck):
                number = np.random.randint(1,6)

                if (number==int(userNumber)): 
                    howmanyrollsaresplendid += 1
        
            if howmanyrollsaresplendid > 0: 
                print(f"you won {howmanyrollsaresplendid} times")
                score += howmanyrollsaresplendid
            else:
                print(f"you lost!")
                score -= 2
                if luck >= 5:
                    luck -= 1
        
            print(f"your score is {score}")

            howmanyrollsaresplendid = 0

            if lastnumberused == userNumber:
                lastnumberusedcount += 1
            else:
                lastnumberusedcount = 0

            lastnumberused = userNumber
    
    if shopping == 0:
        hour += 1
        if hour == 24:
            hour = 0
            day += 1
            print("\n~the dawn of the new day begins~\n")
            with open(f"./saves/save{day}-{name}.txt", "w") as file:
                file.write(f"score~{score},day~{day},felonycount~{felonycount},luck~{luck},name~{name}")
            print("(saved!)")
