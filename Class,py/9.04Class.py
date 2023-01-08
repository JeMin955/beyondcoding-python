# x = list(map(int, input().split()))
# y = int(input())
# check = False
# for i in x:
#     if i == y:
#         check = True

# print(check)
# _______________________________________________________________________
# def binarySearch(number, list):

#     if not list:
#         return False

#     middle = len(list)//2
#     if number > list[middle]:
#         return binarySearch(number, list[middle+1:])
#     elif number < list[middle]:
#         return binarySearch(number, list[:middle])
#     else:
#         return True

# print(binarySearch(1, [1, 2, 3, 4, 5]))
# ___________________________________________________________________________
