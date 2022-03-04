n = int(input())
def nthTermFibonacci(n):
    if n == 0 or n == 1 : 
        return n
    else:
        zeroth = 0
        first = 1
        term = 0
        for i in range(2, n+1):
            term = (zeroth + first) % 10
            zeroth, first = first % 10, term
        return term
print((nthTermFibonacci((n + 2) % 60) - 1) % 10)