def GCD(n): # 欧几里得recursion解法
    a = n[0]
    b = n[1]
    c = 0
    while True: # this will run infinite time until reach the base case
        if b == 0: # base case
            return a
        else:
            c = a % b
            a = b
            b = c
            
            
def naiveGCD(n):
    best = 0
    a = n[0]
    b = n[1]
    for i in range(1,a+b):
        if ((a%i == 0) and (b%i ==0)):
            best = i
    return best

def Greatest(a, b):
    ## input: two positive integer a and b
    ## output: the greatest common divisor of a and b
    if b == 0:
        return a
    else:
        c = a % b
        a = b
        b = c
    return Greatest(a, b)

if __name__ == '__main__':
    # input_num = list(map(int, input().split()))
    # print(GCD(input_num))
    a,b = map(int,input().split())
    print(Greatest(a,b))