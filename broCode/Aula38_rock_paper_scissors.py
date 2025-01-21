import random

user = int(input("""
1 - Pedra
2 - Papel
3 - Tesoura

Escolha: """))

computer = random.randint(1, 3)

plays = ["pedra", "papel", "tesoura"]

print(f"Usuário jogou {plays[user-1]} e computador jogou {plays[computer-1]}")

if user == computer:
    print("Empate")
elif user == 1 and computer == 2 or user == 2 and computer == 3 or user == 3 and computer == 1:
    print("Computador ganhou")
else:
    print("User ganhou")
