from math import *
class AbstractGeometricFigure():
    def __init__(self,side):
        self.side = side

class Circle(AbstractGeometricFigure):
    def __init__(self,radius):
        self.radius = radius
    def info(self):
        print(" Perimetr == {:.3f}\n Area == {:.3f}".format(self.radius*2*pi ,pi*self.radius**2))

class Cylinder(Circle):
    def __init__(self, hight):
        self.hight = hight
        radius = int(input(" Input radius \n "))
        super().__init__(radius)
    def info(self):
        print(" Perimetr == {:.3f}\n Area == {:.3f} \n Volume == {:.3f}".format(self.radius * 4 + 2*self.hight, 2*pi * self.radius ** 2 + 2*pi*self.radius*self.hight, pi*self.radius**2*self.hight))


class Sphere(Circle):
    def __init__(self, hight):
        self.hight = hight
        radius = int(input(" Input radius \n "))
        super().__init__(radius)
    def info(self):
        print(" Area == {:.3f} \n Volume == {:.3f} ".format(4*self.radius **2, (4/3)*pi * self.radius ** 3))

class Triagle(AbstractGeometricFigure):
    def __init__(self, lenght):
        self.lenght = lenght
        super().__init__(side)
    def info(self):
        print(" Perimetr == {:.3f} \n Area == {:.3f}".format(self.side*3,(sqrt(3)*self.side**2)/4))
class Square(AbstractGeometricFigure):
    def info(self):
        print(" Perimetr == ",self.side*4,"\n Area == ",self.side**2)

class Cube(Square):
    def info(self):
        print(" Perimetr == {} \n Area == {} \n Volume == {}".format(12*self.side, 6*self.side**2, self.side**3))

figure = int(input(" Choose the figure: \n Circle   -- 1 \n Cylinder -- 2 \n Sphere   -- 3 \n Triagle  -- 4 \n Square   -- 5 \n Cube     -- 6\n "))


if figure == 1:
    radius = int(input(" Input radius \n "))
    obj1= Circle(radius)
    obj1.info()

elif figure == 2:
    hight = int(input(" Input hight \n "))
    obj2 = Cylinder(hight)
    obj2.info()

elif figure == 3:
    hight = int(input(" Input hight \n "))
    obj3 = Sphere(hight)
    obj3.info()

elif figure == 4:
    side = int(input(" Input side \n "))
    obj4 = Triagle(side)
    obj4.info()

elif figure== 5:
    side = int(input(" Input side \n "))
    obj5 = Square(side)
    obj5.info()

elif figure == 6:
    side = int(input(" Input side \n "))
    obj6 = Cube(side)
    obj6.info()

