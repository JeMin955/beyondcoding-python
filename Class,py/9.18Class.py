# x = int(input())
# y = []
# for i in range(1,x):
#     if i*i <= x:
#         y.append(i)
# if y.count(2):
#     print(False)
# else:
#     print(False)
# __________________________________________________________________
# import threading
# import time

# class Worker(threading.Thread):
#     def __init__(self, n):
#         super().__init__()
#         self.n = n
    
#     def run(self):
#         print(f"thread {self.n} start")
#         time.sleep(2)
#         print(f"thread {self.n} start")

# startTime = time.time()

# threads = []
# print("main thread start")

# for i in range(4):
#     t = Worker(i)
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

# print("main thread end")

# print(time.time() - startTime)

# # def work(n):
# #     print(f"start {n}")
# #     time.sleep(2)
# #     print(f"end {n}")

# # print("main start")
# # for i in range(4):
# #     work(i)

# # print("main end")
