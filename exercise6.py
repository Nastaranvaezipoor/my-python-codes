#تمرین_شماره_ششم
class Shape:
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return (self.width + self.height) * 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius

ashkal = []

print("1. Rectangle")
print("2. Circle")
entekhab = input("Enter choice (1 or 2): ")

if entekhab == "1":
    w = float(input("tool mostatil: "))
    h = float(input("arz mostatil: "))
    ashkal.append(Rectangle(w, h))

elif entekhab == "2":
    r = float(input("shoa dayere: "))
    ashkal.append(Circle(r))

print("\n Hear you are:")

for s in ashkal:
    print("Shape:", type(s).__name__)
    print("Area:", s.calculate_area())
    print("Perimeter:", s.calculate_perimeter())
    print("-" * 20)
