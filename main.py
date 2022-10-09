import math
from random import randint
import turtle


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
        return res1 * res2


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        vertical_distance = self.topright.y - self.bottomleft.y
        horizontal_distance = self.topright.x - self.bottomleft.x

        myturtle.penup()
        canvas.goto(self.bottomleft.x, self.bottomleft.y)
        myturtle.pendown()

        canvas.forward(horizontal_distance)
        canvas.left(90)
        canvas.forward(vertical_distance)
        canvas.left(90)
        canvas.forward(horizontal_distance)
        canvas.left(90)
        canvas.forward(vertical_distance)

        #turtle.done() # this doesnt close canvas before we draw the point

class GuiPoint(Point):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size=10)

        turtle.done()


print("***********************************************************************************")

p10 = Point(randint(0, 200), randint(0, 200))
p11 = Point(randint(200, 400), randint(200, 400))
gui_rectangle = GuiRectangle(p10, p11)

print("Rectangle's Bottom left co-ordinate: ", gui_rectangle.bottomleft.x, gui_rectangle.bottomleft.y)
print("Rectangle's Top right coordinate: ", gui_rectangle.topright.x, gui_rectangle.topright.y)

print("Guess a point within the rectangle range\n")
x = int(input("Enter x: "))
y = int(input("Enter y: "))
p_user = Point(x, y)
gui_point = GuiPoint(p_user.x, p_user.y)


myturtle = turtle.Turtle()
gui_rectangle.draw(canvas=myturtle)
gui_point.draw(canvas=myturtle)
















#
# print("r4 LowerLeft  (", p10.x, ",", p10.y, ")")
# print("r4 UpperRight (", p11.x, ",", p11.y, ")")
#
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
#
# p_user = Point(x, y)
#
# print(p_user.falls_in_rectangle(r4))
# print("------AREA--------")
#
# a_user = int(input("Guess the area: "))
#
# print("Area you guessed: ", a_user)
# print("Actual area of the Rectangle: ", r4.area())






























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
