#Pysearch

import time
from PyDictionary import PyDictionary
dictionary=PyDictionary()
import wikipedia
wikipedia.set_lang("en")


nl = " "

time.sleep(0.5)
print(nl)
print("Hello, you are using Pysearch v0.2")


time.sleep(0.4)
print(nl)
print("Pysearch is a simple program for searching definitions and" "\n" "when you need to research stuff. Also made for fun™")
time.sleep(0.5)
print(nl)
time.sleep(0.5)

action = str(input("Choose an action: 'search def', 'search wiki': "))
print(nl)

if action == "search def":
   input = str(input("Enter a word: "))
   print(nl)
   print("Definition:")
   print(dictionary.meaning(input))
elif action == "search wiki":
     input = str(input("Enter a word/thing: "))
     print(nl)
     print("----------------------WIKIPEDIA.ORG----------------------")
     print(nl)
     print(input, " Wikipedia Summary:")
     print(nl)
     print(wikipedia.summary(input))
     print("---------------------------------------------------------")
else:
    print(action, "is not a command. exiting now")
    print("---------------------------------------------------------")
    time.sleep(1)
    exit()

time.sleep(1)
import AppPackage
exit()


        
   



