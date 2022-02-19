n = int(input())
if n == 0 or n == 1 : 
    print(n)
else:
    zeroth = 0
    first = 1
    term = 0
    for i in range(2, n+1):
        term = zeroth + first
        zeroth, first = first, term
    print(term)