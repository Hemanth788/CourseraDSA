m = int(input())
#  1 5 10
#  28 - 10
#  18 - 10
#  8 - 5
#  3 - 
minimumCoinsRequired = 0
if m >0 :
    while m >= 10 :
        minimumCoinsRequired += 1
        m -= 10
    while m >= 5 :
        minimumCoinsRequired += 1
        m -= 5
    while m >= 1:
        minimumCoinsRequired += 1
        m -= 1
print(minimumCoinsRequired)
