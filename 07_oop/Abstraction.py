from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shape = Circle(5)
print(shape.area())

### Abstraction is like "The Blueprint"
# It hides complex implementation details and shows only the essential features... making it easier for users