import os

path = "C:/Users/Fernando/Documents/RPG.txt"

if os.path.exists(path):
    print("That location exists")
else:
    print("That location doesn't exists")
