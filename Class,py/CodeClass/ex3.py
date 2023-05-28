import time
class Computer:

    count:int = 0
    computers:list = []
    
    def __init__(self, cpu:int, mem:int, ssd:int, mouse:str, keyboard:str, monitor:str):
        self.cpu = cpu
        self.mem = mem
        self.ssd = ssd
        self.mouse = mouse
        self.keyboard = keyboard
        self.monitor = monitor
        Computer.count += 1
        Computer.computers.append(self)

    @staticmethod
    def countComputers():
        print(f"Number of Computer : {Computer.count}")

    @classmethod
    def printMyComputers(cls):
        for computer in cls.computers:
            computer.introduceSpec()

    def introduceSpec(self):
        print(f"CPU : {self.cpu}")
        print(f"MEM : {self.mem}")
        print(f"SSD : {self.ssd}")
        print(f"Mouse : {self.mouse}")
        print(f"Keyboard : {self.keyboard}")
        print(f"Monitor : {self.monitor}")
    
    def calculate(self, a, b):
        startTime = time.time()
        time.sleep(1000 / (self.cpu * self.mem))
        print(a + b)
        print(f"Time Elapsd : {time.time() - startTime}")

class MacBook(Computer):
    def __init__(self, cpu:int, mem:int, ssd:int, mouse:str, keyboard:str, monitor:str, logicpro:bool):
        super().__init__(cpu, mem, ssd, mouse, keyboard, monitor)
        self.logicpro = logicpro

    def introduceSpec(self):
        super().introduceSpec()
        print(f"Install Logicpro : {self.logicpro}")
    



pc1 = Computer(16, 32, 2, "G pro", "Leopord", "Interpixel")
pc2 = Computer(5, 16, 1, "logitech", "NJ 80", "LG")


# pc1.calculate(10, 10)
# pc2.calculate(10, 10)

# Computer.countComputers()
# Computer.printMyComputers()

macbook13 = MacBook(16, 16, 1, "Apple", "Apple", "Apple", True)
macbook13.introduceSpec()