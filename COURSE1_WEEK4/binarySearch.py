length = int(input())
sequence = list(map(int, input().split()))
searchSequenceLength = int(input())
searchSequence = list(map(int, input().split()))
output = []
def binarySearch(key, low, high):
    mid = (low + high) // 2
    if high < low :
        return -1
    if sequence[mid] == key:
        return mid
    elif sequence[mid] > key:
        return binarySearch(key, low, mid - 1)
    else:
        return binarySearch(key, mid + 1,high)
for i in searchSequence:
    output.append(binarySearch(i, 0, length - 1))
print(*output, sep = " ")
