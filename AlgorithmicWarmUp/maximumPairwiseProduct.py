import random
def maxPairwiseProduct1(inputNum) :
    n = len(inputNum)
    maxProduct = 0
    for first in range(n):
        for second in range(first+1, n):
            maxProduct = max(maxProduct, inputNum[first] * inputNum[second])
    return maxProduct

def maxPairwiseProduct2(inputNum) :
    n = len(inputNum)
    first = -1
    second = -1
    for i in range (0 , n) :
        if inputNum[i] > inputNum[first] or first == -1:
            first = i
    for j in range (0 , n) :
        if ((inputNum[j] > inputNum[second] or second == -1)) and j != first:
            second = j
    '''
    print('j:', j)
    print('i:', i)
    print("first:",inputNum[first])
    print("second:",inputNum[second])
    
    print('length of list:',n)
    print('first:',first)
    print('second:', second)
    '''
    try:
        return inputNum[first] * inputNum[second]
    except:
        return print('index error!!!')




if __name__ == '__main__':
    """
    while True :
        randomNum = random.randint(2, 12)
        print(randomNum)
        randomList = []
        for i in range(0, randomNum) :
            n = random.randint(1, 30)
            randomList.append(n)

        print(randomList)
        n1 = maxPairwiseProduct1(randomList)
        n2 = maxPairwiseProduct2(randomList)
    
        if n1 == n2:
            print('OK')
        elif n1 != n2:
            print('Error detected!')
            print(n1)
            print(n2)
            break


    """
    _ = int(input())
    inputNumber = list(map(int, input().split()))
    print(maxPairwiseProduct2(inputNumber))
    