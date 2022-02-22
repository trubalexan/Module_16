class Rectangle:
    def __init__(self, x_coord, y_coord, width, height):
        self.x = x_coord
        self.y = y_coord
        self.width = width
        self.height = height

    def get_rectangle(self):
        return print(f'Rectangle(width = {self.width}, height = {self.height})')

    def get_area(self):
        return self.width * self.height

if __name__ == '__main__':
    rectangle = Rectangle(8, 2, 52, 37)
    rectangle.get_rectangle()
    area = rectangle.get_area()
    print(f'Rectangle area = {area}')