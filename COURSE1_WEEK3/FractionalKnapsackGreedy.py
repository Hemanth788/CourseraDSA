from functools import cmp_to_key
n, capacity = map(int, input().split())
valuesWeightsAndUnitWorths = [0] * n
for i in range(0, n):
    value, weight = map(int, input().split())
    valuesWeightsAndUnitWorths[i] = [value, weight, value/weight]
def compare(x, y):
    return x[2] - y[2]
valuesWeightsAndUnitWorths = sorted(valuesWeightsAndUnitWorths, key = cmp_to_key(compare), reverse = True)
# [[120, 30, 4], [60, 20, 3], [100, 50, 2]]
knapSackValue = 0

for i in valuesWeightsAndUnitWorths :
    if capacity > 0 :
        if capacity >= i[1] :
            capacity -= i[1]
            knapSackValue += i[0]
        else :
            knapSackValue += i[0] * capacity / i[1]
            capacity = 0
    else : 
        break

print(format(knapSackValue, ".4f"))
