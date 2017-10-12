import time
print("     _                ____            _                      ")
time.sleep(0.1)
print("     / \   _ __  _ __ |  _ \ __ _  ___| | ____ _  __ _  ___  ")
time.sleep(0.1)
print("    / _ \ | '_ \| '_ \| |_) / _` |/ __| |/ / _` |/ _` |/ _ \ ")
time.sleep(0.1)
print("   / ___ \| |_) | |_) |  __/ (_| | (__|   < (_| | (_| |  __/ ")
time.sleep(0.1)
print("  /_/   \_\ .__/| .__/|_|   \__,_|\___|_|\_\__,_|\__, |\___| ")
time.sleep(0.1)
print("          |_|   |_|                              |___/       ")
nl = " "
print(nl)
user = str(input("username: "))
print(nl)
print("Hello", user, "you are using AppPackage, a program filled with multiple programs inside!")
print(nl)
searchinput = str(input("Enter program name (all letters lowercase): "))
print(nl)

if searchinput == "pysearch":
   import Pysearch
elif searchinput == "edr":
   import EDR
else:
   print(searchinput, " is not a program. closing now")
   time.sleep(0.4)
   exit()
