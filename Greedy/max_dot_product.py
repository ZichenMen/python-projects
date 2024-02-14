# Find the maximum dot product of two sequences of numbers
# Input: two sequences of n positive integers
# Output: the maximum value of prices

'''
Input format: 
    1st Line: an integer n
    2nd Line: a sequence of integers price 1....price n
    3rd Line: a sequence of integers clicks 1...clicks n
Output format:
    the maximum value of (price1 * clicks 1 + ..... price n * clicks n)

    
Lemma: always pair highest price with highest clicks slot in array

Dot product question
1. find the highest price and clicks
2. add their revenue to total, then pop them out
3. return to step 1
'''

def max_num_index(arr):
    biggest,max_index= 0,0
    for i in range(len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
            max_index = i
    return max_index

def max_ad_revenue(n, price_arr, clicks_arr):
    max_revenue = 0
    price_index, clicks_index = 0,0
    for i in range(n):

        price_index= max_num_index(price_arr)
        clicks_index = max_num_index(clicks_arr)
        max_revenue += price_arr[price_index] * clicks_arr[clicks_index]

        price_arr.pop(price_index)
        clicks_arr.pop(clicks_index)
    return max_revenue


        



if __name__ == '__main__':
    n = int(input())
    price = list(map(int,input().split()))
    clicks = list(map(int,input().split()))
    print(max_ad_revenue(n,price,clicks))
