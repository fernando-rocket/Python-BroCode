# happy = True
# print(happy)

print(happy := True)
print(happy)

foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)
print(foods)

foods = list()
while food := input("What food do you like: ") != "quit":
    foods.append(food)
