# Distinct Summands Problem: Maximum Number of Prizes
# Represent a positive integer as the sum of the maximum number of pairwise distinct positive integers
'''
 Input: An positive integer n

 Output: 
   1st Line: k, the maximum number k such that n can be represented as the sum of k pairwise distinct positive integer
   2nd Line: output k pairwise integers that sum up to n

Safe Choice:  alway take off minimum distinct integer from total,until the sum of integers equal to total. 
                If adding next integer would exceed the total, adjust the last integer that been take off so that sum of cuurent
                integers would equal to total
   

'''


def max_num_prizes(n):
    
    largest_amount, used_candy = 0,0
    total = n
    candy_arr = []

    while used_candy != total:
        
        largest_amount += 1
        used_candy += largest_amount

        if used_candy > total:
            largest_amount = largest_amount * 2 - 1 + total - used_candy
            candy_arr[-1] = largest_amount
            return len(candy_arr), candy_arr
        candy_arr.append(largest_amount)
            
    candy_arr.append(largest_amount)
    return len(candy_arr), candy_arr

def max_num_prizes_gpt(n):
    candy_arr = []
    prize = 1

    while n > 0:
        if n - prize >= 0:
            candy_arr.append(prize)
            n -= prize
            prize += 1
        else:
            # Update the last prize to make the sum equal to the original total.
            candy_arr[-1] += n # -1 refer to last element of array
            n = 0

    return len(candy_arr), candy_arr
   
        




if __name__ == '__main__':
    candy_arr = []
    n, candy_arr= max_num_prizes(int(input()))
    print(n)
    print(" ".join(map(str, candy_arr)))