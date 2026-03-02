import time
import random
from datetime import datetime
now = datetime.now()
#required modules

print("Number Roulette Version 2.01.00")
print("Copyright Void Studios 2026")
time.sleep(0.5); print("\nNO ERRORS REPORTED")
print(now.strftime("DATE: %y-%m-%d"))
#if users see this, program ran correctly

choice = random.randint(1, 10)
odds = 4 / choice
#these are required to make the randomness function

time.sleep(1); print("PROGRAM START.")
print("INITIALIZED\n")

name = input("[NAME] ").upper()
if name == "":
	    print("WELCOME USER")
if name != "":
	    print("WELCOME, " + name)

while True:
    print("\nOPTIONS: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, EXIT")
    user = input("CHOICE: ").upper()
    if user == "EXIT":
        print("PROGRAM END")
        break
    if user not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        print("\nNOT ALLOWED")
        continue
    if int(user) != choice:
        time.sleep(1); print("YOU LOSE. OPPONENTS WIN")
    else:
        time.sleep(1); print("YOU WIN")