def ci(start, end):
    alphas = "abcdefghijklmnopqrstuvwxyz"
    startIndex = alphas.index(start)
    endIndex = alphas.index(end) + 1
    if startIndex > endIndex:
        raise IndexError("start index is larger than end index")
    yield from alphas[startIndex:endIndex]

x = ci('a', 'd')
for i in x:
    print(i)