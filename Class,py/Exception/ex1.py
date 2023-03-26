index, x = map(int,input().split())
N = [100, 200, 1004]

try:
    result = N[index] / x
    print(result)
# except ZeroDivisionError as e:
#     print("0으로 나누냐? : ", e)
# except IndexError as e:
#     print("index를 초과함ㅋ : ", e)
except Exception as e:
    print("예외가 발생했습니다 : ", e)

print("끝")