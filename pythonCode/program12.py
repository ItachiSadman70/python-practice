class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")


class samsung(Phone):
    def photo(self):
        print("You can take photo")

s = samsung()
s.message()
s.call()
s.photo()



class Phone:
    def __init__(self):
        print("I am in phone class")

class Samsung(Phone):
    def __init__(self):
        print("I am in Samsung class")

s = Samsung()



class Shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("The area of the shape")

class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of the triangle: ",area)

class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of the rectangle: ",area)

t1= Triangle(20,30)
t1.area()
r1= Rectangle(14,17)
r1.area()


