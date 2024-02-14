
# Input: 
#   The capacity of a backpack W as well as the weights (w1 ,...,wn) and costs (c1 ,..., cn) of n different compounds.
# Output: 
#   The maximum total   value of fractions of items that fit into the backpack of the given capacity.
'''
Input format: 
    The first line of the input contains the number n of compounds and the capacity W of a backpack. 
    The next n lines define the costs and weights of the compounds. 
    The i-th line contains the cost ci and the weight wi of the i-th compound.
Output format:
    Output the maximum value of compounds that fit into the backpack.

lemma: use as much as possible the most valued items
1. if there is still capacity remain, find the best item, take it as much as possible
2. add and calculate total value
3. reduce the capacity and pop the current item up from array
4. return to frist step
'''

def best_item(costArr,weightArr): # auxiliary method to find the best item
    max_value_per_weight = 0
    best_index = 0

    for i in range(len(costArr)):
        if (costArr[i] / weightArr[i]) > max_value_per_weight:
            max_value_per_weight = costArr[i] / weightArr[i]
            best_index = i
    return best_index


def max_loot(compound_num,capacity,costArr,weightArr):
    total_value = 0
    best_index = 0
    amount_taken = 0
    
    for i in range(compound_num):
        best_index = best_item(costArr,weightArr)
        amount_taken = min(capacity,weightArr[best_index])
        total_value += amount_taken * (costArr[best_index] / weightArr[best_index])
        capacity -= amount_taken
        costArr.pop(best_index)
        weightArr.pop(best_index)
    return round(total_value,4)





if __name__ == '__main__':

    costArr = []
    weightArr = []
    compound_num, capacity = list(map(int,input().split()))

    for i in range(compound_num):
        a, b = list(map(int,input().split()))
        costArr.append(a)
        weightArr.append(b)


    print(max_loot(compound_num,capacity, costArr,weightArr))