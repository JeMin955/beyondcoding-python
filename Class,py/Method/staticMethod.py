class Parent:

    s = "hello"

    @classmethod
    def classMethod(cls, s):
        cls.s = s
        print(f"child method : {cls.s}")
    
    @staticmethod
    def staticMethod(s):
        Parent.s = s
        print(f"static method : {Parent.s}")
    

class Child(Parent):
    pass

parent = Parent()
child = Child()

parent.staticMethod("using static method (parent)")
print(parent.s)
print(child.s)
child.staticMethod("using static method (child)")
print(parent.s)
print(child.s)