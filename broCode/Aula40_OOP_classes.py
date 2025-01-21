class Car:

    num_of_cars = 0

    def __init__(self, make="no info", model="no info", year="no info", color="no info"):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        Car.num_of_cars += 1

    def drive(self):
        print(f"{self.model} is driving")
        return 0

    def stop(self):
        print(f"{self.model} is stopping")
        return 0
