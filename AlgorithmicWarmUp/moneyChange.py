# input: an integer money
# ouput: The minimum number of coins with denominations of 1, 5, 10 that changes money

def moneyChange(n):
    denom = [1 , 5 , 10]
    money = n
    maxCoin = 0
    coinNum = 0
    if money == 0: # base case of recursion
        return 0
    else:
        for i in range(len(denom)):
            if denom[i] <= money:
                maxCoin = denom[i]
        money = money - maxCoin
        coinNum += 1
    return coinNum + moneyChange(money)


if __name__ == '__main__':
    print(moneyChange(int(input())))
    print((5/4))