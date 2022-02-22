class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

# Method to count rectangle Area

    def getArea(self):
        return self.width * self.height


# New class Square

class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a**2
# возведение в степень **2 (в квадрат)

# New class Circle
class Circle:
    def __init__(self, r):
        self.r = r
    def get_area_circle(self):
        return 3.14*(self.r**2)

