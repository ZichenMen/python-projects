# Compute the minumum number of gas tank refills to get from one city to another
# Input: integer d and m, as well as a sequence of integers stop1 < stop2 < ... stop n
# Output: the minimum number of refills to get from one city to another if a car can travel at most m iles on a full tank
'''
input format: 
    1st line: d, distance
    2nd line: m, a car can travel at most m miles on a full tank
    3rd line: n, number of gas station
    last line: stop 1...stop n
output format:
    the minimum refill to reach destination
    if it's impossible, return -1


Lemma: minimum segment problem. Each segment cover as much point as possible
'''



def car_fueling(distance, mile, st_num, st_arr):
    limit = mile
    current_stop = 0
    refill_num = 0
    
    # while the car didnt reach the destination
    while limit < distance:

        
        if current_stop >= st_num or limit < st_arr[current_stop]:
            return -1
        

        # since we're looking at the next station, we need to make sure current_stop + 1 still within the bound of arr
        while current_stop+1 < st_num and st_arr[current_stop+1] <= limit:
            current_stop += 1
        refill_num += 1
        limit = mile + st_arr[current_stop]

        current_stop += 1

    return refill_num




def car_fueling_sample(dist,miles,n,gas_stations):
  
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



if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    s = list(map(int,input().split()))

    print(car_fueling(d, m, n, s))
    