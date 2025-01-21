from Aula40_OOP_classes import Car

carro1 = Car(model="Mercedes")
carro2 = Car(model="Ferrari")

carro1.num_of_cars = 10

carro1.drive()

print(Car.num_of_cars)
print(carro1.num_of_cars)
