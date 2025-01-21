import functools

letters = ["H", "E", "L", "L", "O"]


def unit(x,y):
    print(x)
    print(y)
    print()
    return x+y


word = functools.reduce(unit, letters)
print(word)
print()


def factorial(x,y):
    return x*y


numbers = [x for x in range(1, 10+1)]
print(numbers)
result = functools.reduce(factorial, numbers)
print(result)
