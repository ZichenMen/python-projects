## saffron: 4, 5000
## vanilla: 3, 200
## cinnamon: 5, 10
# input: 1. the number n of compounds, the capacity W of backpack
# 2. the next n line define cost c and weight w of compounds
# output: the maximum value of compounds that fit into backpack

def maxLoot(compNum,totalWeight, compValueList, compCost):
    value = 0
    valueEachComp =[]
    maxCompValue = 0
    for i in range(compNum): # find each comp's value

        valueEachComp.append(compValueList[i] / compCost[i])
    
    
    while totalWeight > 0 or len(valueEachComp) != 0:
        try:
            max_index = valueEachComp.index(max(valueEachComp, default=0)) # index of the most expensive compound
        except:
            break
        
        if compCost[max_index] <= totalWeight:
            fraction = compCost[max_index]
            value += compValueList[max_index]
            totalWeight -= fraction
        else:
            fraction = totalWeight / compCost[max_index]
            value += compValueList[max_index] * fraction
            totalWeight = totalWeight - (compCost[max_index] * fraction)
        compNum -= 1
        compCost.pop(max_index)
        compValueList.pop(max_index)
        valueEachComp.pop(max_index)

    return value

def solve(self, capacity, values,weights):
      res = 0
      for pair in sorted(zip(weights, values), key=lambda x: - x[1]/x[0]):
         if not bool(capacity):
            break
         if pair[0] > capacity:
            res += int(pair[1] / (pair[0] / capacity))
            capacity = 0
         elif pair[0] <= capacity:
            res += pair[1]
            capacity -= pair[0]
      return int(res)

def knapsack(n, capacity, value_list, weight_list):
    unitValues_list = []

    #First lets calculate the unitValues_list
    for i in range (n):
        unitValue = (value_list[i]/weight_list[i])
        unitValues_list.append(unitValue)

    #Now lets fill the knapsack, intake is how much is in the bag at the moment!
    intake = 0
    max_value = 0
    factor = True

    while(factor):
        max_index = unitValues_list.index(max(unitValues_list, default=0)) 
        # this gives the index of the max valued element

        if(weight_list[max_index] <= capacity):
            # In this case, full item is taken in
            intake = weight_list[max_index]
            capacity -= weight_list[max_index]
            max_value += value_list[max_index]

        else:
            # weight_list[max_index] > capacity
            # In this case, fraction to be taken
            fraction = capacity / weight_list[max_index] 
            max_value += value_list[max_index]*fraction
            capacity = int(capacity - (weight_list[max_index] * fraction))

        weight_list.pop(max_index)
        value_list.pop(max_index)
        unitValues_list.pop(max_index)
        print(weight_list)

        n -= 1 #no. of items left
        factor = ((n != 0) if ((capacity != 0) if True else False) else False)

    return max_value

            



if __name__ =='__main__':
    
    compCost = []
    compValueList = []

    compNum , totalWeight = map(int, input().split())
    for i in range(compNum):
        a , b = map(int, input().split())
        compCost.append(a)
        compValueList.append(b)
        

    print(maxLoot(compNum, totalWeight, compCost, compValueList))
    '''

    value_list = []
    weight_list = []

    #The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack. 
    #The next 𝑛 lines define the values and weights of the items. 

    n , capacity = map(int, input('n, capacity: ').split())

    for i in range (n):
        value , weight = map(int, input('value, weight: ').split())
        value_list.append(value)
        weight_list.append(weight)

    #Output the maximal value of fractions of items that fit into the knapsack.
    print("{:.10f}".format(knapsack(n, capacity, value_list, weight_list)))
    '''