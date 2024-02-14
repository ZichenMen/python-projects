# first line: integer d, distance between the cities
# second line: integer m, a car can travel at most on full tank
# integer n, number of gas stations
# n integers, distances of each station

def carFueling(totalDistance, fullFuelTravel, stationNum, stationDist):
    refuelCount = 0
    previousStation = 0
    currentFuel = fullFuelTravel
    stationDist.append(totalDistance) #u需要append终点站进list，否则会index out of range
    for i in range(stationNum):
        currentStation = int(stationDist[i])
        nextStation = int(stationDist[i + 1])
        
        currentFuel = currentFuel - (currentStation - previousStation)
        requiredFuel = nextStation - currentStation

        if requiredFuel > fullFuelTravel:
            return -1
        
        if requiredFuel >= currentFuel:
            refuelCount += 1
            currentFuel += fullFuelTravel ## 重点，如果相等的话，+=
            '''
            print('i:',i)
            print('refuel count:',refuelCount)
            print('current fuel:',currentFuel)
            '''
            
            
        previousStation = currentStation

    return refuelCount


def car_fueling(dist,miles,n,gas_stations):
  
    num_refill, curr_refill, limit = 0,0,miles
    while limit < dist:  
        # While the destination cannot be reached with current fuel
        if curr_refill >= n or gas_stations[curr_refill] > limit:
            # Cannot reach the destination nor the next gas station
            return -1
          
        # Find the furthest gas station we can reach
        while curr_refill < n-1 and gas_stations[curr_refill+1] <= limit:
            curr_refill += 1
            
        num_refill += 1  # Stop to tank
        limit = gas_stations[curr_refill] + miles  # Fill up the tank 
        curr_refill += 1
        
    return num_refill


if __name__ =='__main__':
    d = int(input())
    m = int(input())
    _ = int(input())
    g = list(map(int, input().split()))
    print(car_fueling(d , m , _ , g))