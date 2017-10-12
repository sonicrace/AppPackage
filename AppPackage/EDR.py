#Enemy Difficulty Rating

import time
nl = " "
print(">ENEMY DIFFICULTY RATING PROGRAM")
time.sleep(0.2)
print(nl)
time.sleep(0.2)
enguess = float(input("On a scale of 1-10 how high would you rate the difficulty of the opponent: "))
print(nl)
time.sleep(0.5)
enpatterns = float(input("How many different attack patterns does the enemy have? '0' if none: "))
print(nl)
time.sleep(0.5)
enpamount = float(input("How many attacks in each pattern: "))
print(nl)
time.sleep(0.5)
enhealth = float(input("Enter Enemy Health: "))
print(nl)
time.sleep(0.5)
plhealth = float(input("Enter Player Health: "))
print(nl)
time.sleep(0.5)
encrit = float(input("What is the chance of a critical hit? (remove percent sign): "))
print(nl)
time.sleep(0.5)
enavgdmg = float(input("What is the average attack damage? "))
print(nl)
time.sleep(0.5)
encritdmg = float(input("What is the damage when it is a critical hit: "))
print(nl)
time.sleep(0.5)
entype = str(input("What would you classify this enemy as: regular, miniboss, boss: "))
print(nl)

totaldmgperpattern = float(enavgdmg * enpamount)
plkill = float(plhealth / enavgdmg)
rawdr = float(totaldmgperpattern / plkill * enpatterns)
edr = float(rawdr / 10)
print("ENEMY DIFFICULTY RATING: ", edr)

time.sleep(1)
print("---------------------------------------------------------")
import AppPackage
exit()




                 
              
