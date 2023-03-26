import random
pw = str(random.randrange(0, 999999))
n = []
for i in pw:
    for j in range(0, 10):
        j = str(j)
        if i == j:
            n.append(j)
            break
print(f"Password is {''.join(n)}")