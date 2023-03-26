def zihyo(num):
    x = 10 / num
    if x % 1 != 0:
        raise Exception("result is not integer")

try:
    zihyo(int(input))
except Exception as e:
    print("Exception : ", e)