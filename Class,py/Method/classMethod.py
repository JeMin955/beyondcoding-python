class Rectangle:

    rectCount = 0

    def __init__(self, w, h):
        self.width = w
        self.height = h
        Rectangle.rectCount += 1

    def printRect(self):
        print(self.width, self.height)

    @classmethod
    def printRectCount(cls):
        print(cls.rectCount)

    @staticmethod
    def testStaticMethod():
        print("haha")


rect1 = Rectangle(10, 20)
rect2 = Rectangle(1, 2)

rect1.printRect()
rect2.printRect()

Rectangle.printRectCount()
Rectangle.testStaticMethod()