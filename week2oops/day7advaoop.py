print("1. ANIMAL INHERITANCE AND POLYMORPHISM")
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
    def __str__(self):
        return f"Animal Name: {self.name}"
class Dog(Animal):
    def speak(self):
        print(self.name, "says Bowbow!")
class Cat(Animal):
    def speak(self):
        print(self.name, "says meowmeow!")
dog_name = input("Enter dog name: ")
cat_name = input("Enter cat name: ")
dog = Dog(dog_name)
cat = Cat(cat_name)
animals = [dog, cat]
print("\nPolymorphism Example:")
for animal in animals:
    animal.speak()


print("\n2. SHAPE INHERITANCE")
class Shape:
    def __init__(self, name):
        self.name = name
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
length = float(input("\nEnter rectangle length: "))
width = float(input("Enter rectangle width: "))
radius = float(input("Enter circle radius: "))
rectangle = Rectangle(length, width)
circle = Circle(radius)
print("Rectangle Area:", rectangle.area())
print("Circle Area:", circle.area())