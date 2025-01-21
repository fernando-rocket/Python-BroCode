class Organism:
    alive = True


class Animal(Organism):
    def eat(self):
        print("This animal is eating")


class Dog(Animal):
    def bark(self):
        print("This dog is barking")


dohu = Dog()

print(dohu.alive)
dohu.eat()
dohu.bark()