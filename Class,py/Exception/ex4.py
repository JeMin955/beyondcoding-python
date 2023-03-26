from shutil import ExecError


class NotFactorOfTenError(Exception):
    def __init__(self):
        super().__init__("the number is not factor of 10")

    def zihyo(num):
        x = 10 / num
        if x % 1 != 0:
            raise NotFactorOfTenError
        print(x)

    zihyo(100)