import math
def optimal_summands(n):
    k = ((1 + 8*n)**0.5 - 1) / 2
    print(k)
    k = math.ceil(k)
    summands = list(range(1, k+1))
    print(summands)
    the_sum = int(k * (k+1) / 2)
    if the_sum - n > 0:
        print(the_sum - n, the_sum - n - 1)
        del summands[the_sum-n-1]
    return summands
x = optimal_summands(int(input()))
print(len(x))
print(*x, sep = " ")

