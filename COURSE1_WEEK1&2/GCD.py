a, b = map(int, input().split(" "))
def GCD(a, b):
    if b == 0:
        print(a)
    else:
        GCD(b, a%b)
GCD(a, b)