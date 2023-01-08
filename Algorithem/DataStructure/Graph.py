#graph1 = {}
#for _ in range(4):
#    x, y = map(int, input().split())
#    if x in graph1:
#        graph1[x].append(y)
#    else:
#        graph1.update({x:[y]})
#    if y in graph1:
#        graph1[y].append(x)
#    else:
#        graph1.update({y:[x]})
#print(graph1)


graph2 = [[0]*5 for _ in range(5)]
for _ in range(4):
    i, j = map(int, input().split())
    graph2[i][j] = graph2[j][i] = 1
print(graph2)