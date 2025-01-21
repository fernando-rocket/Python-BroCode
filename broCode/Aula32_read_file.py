# Fecha automaticamente o arquivo
with open("C:/Users/Fernando/Documents/RPG.txt") as doc:
    print(doc)

# Não fecha automaticamente o arquivo
document = open("C:/Users/Fernando/Documents/RPG.txt", "rt")
print(document.read())
document.close()
