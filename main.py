import math
from tkinter import Y
from geometry import PPoint
from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Point_in_rect(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False

    def in_rect(self, rectangle):
        if rectangle.bottomleft[0] < self.x < rectangle.topright[0] and rectangle.bottomleft[1] < self.y < \
                rectangle.topright[1]:
            return True
        else:
            return False

    def falls_in_rectangle(self, rectangle):  # referring variables of object type Point
        if rectangle.bottomleft.x < self.x < rectangle.topright.x and rectangle.bottomleft.y < self.y < rectangle.topright.y:
            return "YES! Point lies in the range of Rectangle!"
        else:
            return "NOPE! Point does not lie in the range of Rectangle!"

    def distance(self, p):
        res1 = (p.x - self.x) ** 2
        res2 = (p.y - self.y) ** 2
        return math.sqrt(res1 + res2)


class Rectangle:

    def __init__(self, bottomleft, topright):
        self.bottomleft = bottomleft
        self.topright = topright

    def area(self):
        res1 = (self.topright.x - self.bottomleft.x)
        res2 = (self.topright.y - self.bottomleft.y)
        return res1*res2

print("***********************************************************************************")
p10 = Point(randint(1, 5), randint(1, 5))
p11 = Point(randint(5, 10), randint(5, 10))
r4 = Rectangle(p10, p11)

print("r4 LowerLeft  (", p10.x, ",", p10.y, ")")
print("r4 UpperRight (", p11.x, ",", p11.y, ")")

x = int(input("Enter x: "))
y = int(input("Enter y: "))

p_user = Point(x, y)

print(p_user.falls_in_rectangle(r4))
print("------AREA--------")

a_user = int(input("Guess the area: "))

print("Area you guessed: ", a_user)
print("Actual area of the Rectangle: ", r4.area())













# p1 = Point(1, 1)
# p2 = Point(5, 5)
# p3 = Point(0, 0)
# p4 = Point(3, 3)
# p5 = Point(-2, -2)
# p6 = Point(5, 5)
#
# r1 = Rectangle(p1, p2)
# print(r1.area())
# r2 = Rectangle((-5, -5), (0, 0))
#
# p7 = Point(randint(1, 5), randint(1, 5))
# p8 = Point(randint(5, 10), randint(5, 10))
# p9 = Point(randint(0, 10), randint(0, 10))
# r3 = Rectangle(p7, p8)

# print(p3.falls_in_rectangle(r1))
# print(p4.falls_in_rectangle(r1))

# print(p5.in_rect(r2))
# print(p6.in_rect(r2))
# print(p1.)
# print(p1.distance(p2))

# print("r3 LowerLeft  (", p7.x, ",", p7.y, ")")
# print("r3 UpperRight (", p8.x, ",", p8.y, ")")
#
# print("Is the point (", p9.x, ",", p9.y, ") in rectangle r3: ", p9.falls_in_rectangle(r3))
