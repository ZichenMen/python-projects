def GCD(n):
    a = n[0]
    b = n[1]
    c = 0
    while True:
        if b == 0:
            return a
        else:
            c = a % b
            a = b
            b = c
            
def LCM(n):
    a = n[0]
    b = n[1]
    c = 0
    x = n[0]
    y = n[1]
    while True:
        if b == 0:
            break
        else:
            c = a % b
            a = b
            b = c
    return int(x / a * y)
    
# the lcm of a and b is their product divided by their gcd


def LCM2(a , b):
    # Input: two positive integer a and b
    # Output: the least common multiple of a and b

    product = a * b

    while True:
        if b == 0:
            return int(product / a)
        else:
            c = a % b
            a = b
            b = c
    
    ## now we find a is GCD, then calculate LCM
    


if __name__ == '__main__':
    #input_num = list(map(int, input().split()))
    #print(LCM(input_num))
    a, b = map(int, input().split())
    print(LCM2(a,b))