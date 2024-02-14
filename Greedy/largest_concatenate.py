# Largest Concatenate Problem: Maximum Salary
# Compile the largest number by concatenating the given numbers
# Input: A sequence of positive integers
# Output: The largest number that can be obtained by concatenating the given integers in some order



def max_salary(int_num, int_arr):
    best_num = "0"
    best_index = -1
    sequence = []
    while len(int_arr) != 0:
        best_num = "0"
        for i in range(len(int_arr)):
            if int_arr[i] * 3 > best_num * 3:
                best_num = int_arr[i]
                best_index = i
        sequence.append(best_num)
        int_arr.pop(best_index)
    return sequence




if __name__ == '__main__':

    int_num = int(input())
    int_arr = list(map(str,input().split()))
    str_arr = max_salary(int_num, int_arr)
    print("".join(str_arr))