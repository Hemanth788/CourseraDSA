n = int(input())
PPC = sorted(list(map(int , input().split())))
CPD = sorted(list(map(int , input().split())))
revenue = 0
for i in range(n):
    revenue += PPC[i] * CPD[i]
print(revenue)