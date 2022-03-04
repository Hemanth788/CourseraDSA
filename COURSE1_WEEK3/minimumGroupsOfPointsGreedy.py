from functools import cmp_to_key


n = int(input())
points = []
noOfLines = 1
AnswerPoints = []
for i in range(n):
    points.append(list(map(int , input().split(" "))))
def compare(x, y):
    return x[1] - y[1]
points = sorted(points, key = cmp_to_key(compare))
print(points)
leftMostSegmentRightEndPoint = points[0][1]
AnswerPoints.append(leftMostSegmentRightEndPoint)
for i in range(1, len(points)):
    if leftMostSegmentRightEndPoint < points[i][0] or leftMostSegmentRightEndPoint > points[i][1]:
        print(leftMostSegmentRightEndPoint)
        leftMostSegmentRightEndPoint = points[i][1]
        print(leftMostSegmentRightEndPoint)
        noOfLines += 1
        AnswerPoints.append(leftMostSegmentRightEndPoint)
    

print(noOfLines)
for i in range(len(AnswerPoints)):
    if i == len(AnswerPoints) - 1 :
        print(AnswerPoints[i])
    else:
        print(AnswerPoints[i], end = " ")
