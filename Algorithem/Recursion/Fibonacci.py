def fibonacci(n):
    if n < 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

def optfi(n, before1=1, before2=1):
    if n < 2:
        return before1
    
    return optfi(n-1, before1+before2, before1)

print(optfi(5))