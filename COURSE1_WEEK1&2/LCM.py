a, b = map(int, input().split(" "))
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)
def LCM(a, b):
    print((a*b) // GCD(a, b))
LCM(a, b)