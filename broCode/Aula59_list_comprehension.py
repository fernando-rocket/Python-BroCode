squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)

squares_2 = [x*x for x in range(1, 11)]
print(squares_2, " squares")

pares = [x for x in range(11) if x % 2 == 0]
print(pares, " pares")
