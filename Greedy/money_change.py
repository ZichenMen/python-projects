## Money Change Problem
## Compute the minimum number of coins to change the given value with denominations 1, 5, 10
# input: integer money
# output: the minimum number of coins


def money_change(n):
    num = 0
    while n != 0:
        if n >= 10:
            n -= 10
            num = num + 1
        elif n >= 5:
            n -= 5
            num = num + 1
        else:
            n -= 1
            num = num + 1
    return num

def optimized_money_change(n):
    num = 0
    num = n // 10
    n = n % 10

    num = n // 5
    n = n % 5

    num = num + n

    return n





if __name__ == '__main__':
    print(money_change(int(input())))