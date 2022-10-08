class PPoint:

    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y
        print("Constructor called!")

    def setY(self, Y):
        self.y=Y


pp1 = PPoint()
print(pp1.x)

pp1.setY(10)

print(pp1.y)