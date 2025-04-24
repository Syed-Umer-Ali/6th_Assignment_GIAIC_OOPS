from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

    
 # Create a Rectangle object
rectangle = Rectangle(5, 3)
print(f"Rectangle area: {rectangle.area()}") 