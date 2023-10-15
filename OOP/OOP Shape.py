class shape:
    def __init__(self):
        self.__areavalue = 0
        self.__perimetervalue = 0

    def area(self):
        print("Area ", self.__areavalue)
    def perimeter(self):
        print("Perimeter ", self.__perimetervalue)

class rectangle(shape):
    def __init__(self, length, breadth):
        shape.__init__(self)
        self.__length = length
        self.__breadth = breadth

    def area(self):
        self.__areavalue = self.__length * self.__breadth
        print("Area ", self.__areavalue)

class circle(shape):
    def __init__(self, radius):
        shape.__init__(self)
        self.__radius = radius
    def area(self):
        self.__areavalue = self.__radius * 3.142
        print("Area ", self.__areavalue)

myCircle = circle(20)
myCircle.area()

myRectangle = rectangle(10,17)
myRectangle.area()