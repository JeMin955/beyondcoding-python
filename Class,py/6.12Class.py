#STACK은 append와 pop으로 더하고 뺄 수 있다.
#push()
#pop()
#top()
#bottem()

# class Stack:

#     def __init__(self):
#         self.x = []

#     def push(self,a):
#         self.x.append(a)

#     def pop(self):
#         if self.empty():
#             print("x가 비어있습니다")
#         else:
#             self.x.pop()

#     def top(self):
#         if self.empty():
#             print("x가 비어있습니다")
#         else:
#             return self.x[-1]

#     def bottom(self):
#         if self.empty():
#             print("x가 비어있습니다")
#         else:
#             return self.x[0]

#     def empty(self):
#         return not bool(len(self.x)) 

# y = input()

# stack = Stack()

# def test_func(y):
#     for i in y:
#         if i == "(":
#             stack.push("(")
#         else:
#             if stack.empty():
#                 print("False")
#                 return
#             stack.pop()

#     if stack.empty():
#         print("true")
#     else:
#         print("False")

# test_func(y)