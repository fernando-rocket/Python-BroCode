from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive a car")

    def stop(self):
        print("This car stopped")


class Motocycle(Vehicle):
    def go(self):
        print("You ride a motocycle")

    def stop(self):
        print("This motocycle stopped")


# vehicle = Vehicle()
car = Car()
motocycle = Motocycle()

# vehicle.go()
car.go()
motocycle.go()
