from cmath import inf


size = int(input())
sequence = list(map(int, input().split(' ')))
max = float("-inf")
secondMax = float("-inf")
# 5 6 2 7 4
for i in sequence : 
    if max <= i : 
       secondMax, max  = max, i
    elif secondMax <= i:
        secondMax = i
print(max*secondMax)

