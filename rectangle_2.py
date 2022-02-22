from Rectangle import Rectangle, Square

# далее создаём два прямоугольника

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

# вывод площади наших двух прямоугольников
print(rect_1.getArea())
print(rect_2.getArea())


# вывод площади наших двух квадратов
square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(), square_2.get_area_square())

figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.getArea())
