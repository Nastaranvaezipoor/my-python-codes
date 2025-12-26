#تمرین_شماره_شش_که_در_انتهای_فایل_پنج_بود
class Vehicle:
    def __init__(self, brand, year, price):
        self.brand = brand
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price} Tomans")

class Car(Vehicle):
    def __init__(self, brand, year, price, num_doors):
        super().__init__(brand, year, price)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, price, has_sidecar):
        super().__init__(brand, year, price)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        status = "Yes" if self.has_sidecar else "No"
        print(f"Has Sidecar: {status}")

cars = [
    Car("BMW M4", 2024, "12,000,000,000", 2),
    Car("Mercedes-Benz S-Class", 2025, "15,500,000,000", 4),
    Car("JAC S5", 2023, "1,800,000,000", 4)
]

motos = [
    Motorcycle("Honda CBR", 2021, "950,000,000", False),
    Motorcycle("KTM Adventure", 2024, "1,200,000,000", True)
]

print("--- Welcome to the Showroom ---")
print("1. Cars")
print("2. Motorcycles")
category = input("\nSelect category (1 or 2): ")

if category == "1":
    print("\n--- Available Cars ---")
    for i in range(len(cars)):
        print(f"{i+1}. {cars[i].brand}")
    choice = int(input("\nSelect a car: ")) - 1
    print("\n" + "="*20)
    cars[choice].display_info()
    print("-------------------")

elif category == "2":
    print("\n--- Available Motorcycles ---")
    for i in range(len(motos)):
        print(f"{i+1}. {motos[i].brand}")
    choice = int(input("\nSelect a motorcycle: ")) - 1
    print("\n-------------------")

    motos[choice].display_info()
    print("-------------------")
