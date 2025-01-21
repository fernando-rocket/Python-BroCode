import os
import shutil

if not os.path.exists("C:/Users/Fernando/Documents/teste.txt"):
    f = open("C:/Users/Fernando/Documents/teste.txt", "x")
    f.close()

action = int(input("Ação: "))

if action == 1:
    try:
        os.remove("C:/Users/Fernando/Documents/teste.txt") # Files
    except:
        print("File não existe")

if action == 2:
    try:
        os.rmdir("C:/Users/Fernando/Documents/pastateste") # Exclui Pastas VAZIAS!!!
    except FileNotFoundError:
        print("Pasta não existe")
    except OSError:
        print("Não pode excluir pastas com conteúdo")

if action == 3:
    shutil.rmtree("C:/Users/Fernando/Documents/pastateste")
