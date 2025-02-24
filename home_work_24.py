import re

class Car:
    def __init__(self, year, manufacturer, model, fuel_consumption, dealer_price):
        self.year = year
        self.manufacturer = manufacturer
        self.model = model
        self.mileage = 0  # Пробіг за замовчуванням 0
        self.fuel_consumption = float(fuel_consumption)
        self.dealer_price = dealer_price

    def drive(self):
        print(f"Я авто марки {self.model}, їду по справам господаря")

    @property
    def category(self):
        return "Крутяк" if self.dealer_price > 15000 else "тачелла"


car1 = Car(2020, "Toyota", "Camry", 7.5, 20000)
car2 = Car(2018, "Ford", "Focus", 6.8, 12000)
car3 = Car(2022, "BMW", "X5", 9.5, 50000)

car2.mileage = 30000

car1.drive()

print(car1.category)
print(car2.category)
print(car3.category)