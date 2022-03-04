# go to the farthest station possible from one point to another
totalDistance = int(input())
maxDistanceWithFullTank = int(input())
noOfStations = int(input())
distancesBetweenStops = [0]
distancesBetweenStops.extend(list(map(int, input().split())))
# A = 0<= 1<= 2 <= ... <= noOfStations <= noOfStations + 1 = B
distancesBetweenStops.append(totalDistance)
minimumRefills = 0
currentRefill = 0
while currentRefill <= noOfStations : 
    lastRefill = currentRefill
    while currentRefill <= noOfStations and distancesBetweenStops[currentRefill + 1] - distancesBetweenStops[lastRefill] <= maxDistanceWithFullTank:
        currentRefill += 1
    if currentRefill == lastRefill : 
        minimumRefills = -1
        break
    if currentRefill <= noOfStations:
        minimumRefills += 1
print(minimumRefills)
