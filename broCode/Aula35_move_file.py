import os

source = "C:/Users/Fernando/Documents/RPG.txt"

destination = "C:/Users/Fernando/Documents/code/RPG.txt"

if os.path.exists("C:/Users/Fernando/Documents/RPG.txt"):
    os.replace(source, destination)
else:
    os.replace(destination, source)
