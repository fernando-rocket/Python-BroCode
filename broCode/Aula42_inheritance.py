class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleeping(self):
        print("This animal is sleeping")


class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")


class Fish(Animal):
    def swin(self):
        print("This fish is swimming")


class Hawk(Animal):
    def fly(self):
        print("This animal is flying")


coelho = Rabbit()

print(coelho.alive)
coelho.eat()
coelho.sleeping()
coelho.run()
