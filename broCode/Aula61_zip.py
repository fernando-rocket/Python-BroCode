names = ["Dude", "Bro", "Mister"]
passwords = ("password", "abc123", "guest")

lista = [(x, y) for x, y in zip(names, passwords)]

print(lista)
