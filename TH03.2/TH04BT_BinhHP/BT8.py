class Person:
    def __init__(self,name, year, height, weight):
        self.name = name
        self.year = year
        self.height = height
        self.weight = weight

    def Geeting(self):
        return f"My name is: {self.name}\nYear: {self.year}\nHeight: {self.height}m\nWeight: {self.weight}"
    def BMI(self):
        bmi = round(self.weight / (self.height ** 2), 2)
        return f"Chỉ số BMI: {bmi}"

p1 = Person('Hoàng Phú Bình', 2004, 1.75, 57)
print(p1.Geeting())
print(p1.BMI())