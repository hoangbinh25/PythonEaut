class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        area = round(self.width * self.height, 1)
        return area

    def getPerimeter(self):
        perimeter = round((self.width + self.height) * 2, 1)
        return perimeter

while True:
    x = float(input("Nhập chiều rộng: "))
    y = float(input("Nhập chiều dài: "))

    if x <= 0 or y <= 0:
        print('Nhập chiều rộng > 0 và chiều dài > 0: ', x, y)
    else:
        rect = Rectangle(x, y)
        print('---- Thuộc tính ------------')
        print('1. Thuộc tính Chiều rộng: ', rect.width)
        print('2. Thuộc tính Chiều dài: ', rect.height)

        dt = rect.getArea()
        cv = rect.getPerimeter()
        print('------ Phương thức ------')
        print('1. Phương thức tính Diện tích: ', dt)
        print('2. Phương thức tính Chu vi: ', cv)