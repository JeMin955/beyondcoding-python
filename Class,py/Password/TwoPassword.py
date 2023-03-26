import random
gadget = "abcdefghijklmnopqrstuvwxyz0123456789"
PASSWORD = random.choice(gadget) + random.choice(gadget) + random.choice(gadget) + random.choice(gadget)
x = "abcdefghijklmnopqrstuvwxyz0123456789"
n = []
for i in PASSWORD:
    for j in x:
        j = str(j)
        if i == j:
            n.append(j)
            break
print(f"Password is {''.join(n)}")