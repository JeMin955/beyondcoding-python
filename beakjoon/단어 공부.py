n = input()
n = n.upper()
d = {}
x = []
for i in n:
    if i in d.keys():
        d[i]+=1
    else:
        d.update({i:1})
t = list(d.values())
x.append(t)
if x[0].count(max(x[0])) > 1 :
    print("?")
else:
    print(list(d.keys())[list(d.values()).index(max(x[0]))])