import re

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand  # Фірма крута
        self.model = model  # Моделька топ

    def info(self):
        print(f"Це {self.brand} {self.model}, короч, норм тачка")


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors  # Двері, шоб заходить

    def info(self):
        print(f"Це {self.brand} {self.model}, дверей: {self.num_doors}, пушка гонка!")


class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type  # Вел не просто вел, а якийсь

    def info(self):
        print(f"Це {self.brand} {self.model}, вел {self.bike_type}, можна на задньому катати!")


class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity  # Вантаж бере, як батя сумки

    def info(self):
        print(f"Це {self.brand} {self.model}, тягне {self.capacity} тонн, машина-звір!")


car = Car("Toyota", "Camry", 4)
bike = Bike("Trek", "Marlin 7", "гірський")
truck = Truck("Volvo", "FH16", 25)

car.info()
bike.info()
truck.info()
