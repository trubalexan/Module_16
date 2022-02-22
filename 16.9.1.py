class Dot:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    def get_dot(self):
        return print(f'Dot({self.x}, {self.y})')

class Line:
    def __init__(self, x_coord, y_coord, angle, lsize):
        self.x = x_coord
        self.y = y_coord
        self.angle = angle
        self.lsize = lsize

    def get_line(self):
        return print(f'Line({self.x}, {self.y}, {self.angle}, {self.lsize})')

class Triangle:
    def __init__(self, x_coord, y_coord, angle1, lsize1, angle2, lsize2, angle3, lsize3):
        self.x = x_coord
        self.y = y_coord
        self.angle1 = angle1
        self.lsize1 = lsize1
        self.angle2 = angle2
        self.lsize2 = lsize2
        self.angle3 = angle3
        self.lsize3 = lsize3

    def get_triangle(self):
        return print(f'Triangle({self.x}, {self.y}, {self.angle1}, {self.lsize1}, {self.angle2}, {self.lsize2}, {self.angle3}, {self.lsize3})')

class Rectangle:
    def __init__(self, x_coord, y_coord, width, height):
        self.x = x_coord
        self.y = y_coord
        self.width = width
        self.height = height

    def get_rectangle(self):
        return print(f'Rectangle({self.x}, {self.y}, {self.width}, {self.height})')


class Circle:
    def __init__(self, x_coord, y_coord, rad):
        self.x = x_coord
        self.y = y_coord
        self.rad = rad

    def get_circle(self):
        return print(f'Circle({self.x}, {self.y}, {self.rad})')


if __name__ == '__main__':
    dot = Dot(5, 6)
    dot.get_dot()

    line = Line(5, 6, 30, 45)
    line.get_line()

    triangle = Triangle(7, 8, 90, 2, 315, 2.8284, 315, 2)
    triangle.get_triangle()

    rectangle = Rectangle(8, 2, 52, 37)
    rectangle.get_rectangle()

    circle = Circle(4, 12, 25)
    circle.get_circle()