from functools import cmp_to_key


def largest_number(a):
    return ''.join(sorted(a, key=cmp_to_key(lambda x, y: -1 if int(x + y) < int(y + x) else 1), reverse=True))

n = int(input())
a = list(map(str, input().split(" ")))
print(largest_number(a))

