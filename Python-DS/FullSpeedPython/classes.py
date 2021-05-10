class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def width(self):
        return self.x2-self.x1

    def height(self):
        return self.y1-self.y2

    def area(self):
        width = self.width()
        height = self.height()
        return width*height

    def perimeter(self):
        width = self.width()
        height = self.height()
        return 2*(width + height)

    def __str__(self):
        return str(self.x1) + ', ' + str(self.y1) + ', ' \
                    + str(self.x2) + ', ' + str(self.y2)


class Square(Rectangle):
    def __init__(self, x1, y1, length):
        x2 = x1 + length
        y2 = y1 + length
        super().__init__(x1, y1, x2, y2)


rect = Rectangle(0, 5, 3, 1)
print(rect.width())
print(rect.height())
print(rect.area())
print(rect.perimeter())
print(rect)


class Animal ():
    def __init__(self, name, food, characteristic):  # Animal's constructor
        self.name = name  # Animal's attribute
        self.characteristic = characteristic  # Animal's attribute
        self.food = food  # Animal's attribute
        print("I am a " + str(self.name) + ".")


class Mammal (Animal):  # Mammal inherits from Animal
    def __init__(self, name, food):  # Mammal's constructor
        Animal.__init__(self,
                        name,
                        food,
                        "warm blooded")  # Animal's constructor
        print("I am warm blooded.")


class Carnivore (Mammal):  # Carnivore inherits from Mammal
    def __init__(self, name):  # Carnivore's constructor
        Mammal.__init__(self, name, "meat")  # Mammal's constructor
        print("I eat meat.")


lion = Carnivore("lion")  # lion is an instance of Carnivore


class Person(object):  # Super class
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi, I'm " + self.name + ".")  # Super class does something


class Student(Person):  # Subclass inheriting from the super class
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree
        super().__init__(name)  # calls constructor of super class

    def greet(self):
        super().greet()  # calls method of super class
        print("I am a " + self.degree + " student.")


student = Student("Ali", "PhD")  # Create an object of the subclass
student.greet()
