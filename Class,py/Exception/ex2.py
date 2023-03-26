try:
    x = int(input())
    y = (10 / x)
except Exception as e:
    print(e)
else:
    print(y)
finally:
    print("어쨌든 끝났다(쩝)")