n, m = map(int, input().split(" "))
def pisanoPeriodLengthFunction(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
        if (previous == 0 and current == 1): 
            print("pisanoPeriodLengthFunction", i+1)
            return i + 1

def modifiedN(n, m):
    pisanoPeriodLength = pisanoPeriodLengthFunction(m)
    modifiedN = n % pisanoPeriodLength
    print("modifiedN", modifiedN)
    return modifiedN

def nthTermFibonacci(n):
    if n == 0 or n == 1 : 
        return n
    else:
        zeroth = 0
        first = 1
        term = 0
        for i in range(2, n+1):
            term = zeroth + first
            zeroth, first = first, term
        return term

def fiboModM(n, m):
    print(nthTermFibonacci(modifiedN(n, m)) % m)

fiboModM(n, m)


