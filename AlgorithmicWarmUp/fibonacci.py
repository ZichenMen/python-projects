def febRecurs(n):
    if n <= 1:
        return n
    else:
        return febRecurs(n-1) + febRecurs(n-2)

def febRecursFast(n):
    a = 0
    b = 1
    if n < 0:
        return 0
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(1, n): 
            c = a + b
            a = b ## a继承着f(n-2)上上个f的结果 previous
            b = c ## b继承着f（n-1）上个f的结果 current
        #从1开始算的加法
        return b



def pisanoPeriod(m): # calculate the length of pisano period
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current \
        = current, (previous + current) % m
         
        # A Pisano Period starts with 01
        if (previous == 0 and current == 1): # when a == 0 and b == 1, it means the period has ended and bring to the start
            return i + 1 # stop the loop when it finds the occurence of 0 and 1 in the sequence
 
# Calculate Fn mod m
def fibonacciModulo(n, m):
     
    # Getting the period
    pisano_period = pisanoPeriod(m)
     
    # Taking mod of N with
    # period length
    n = n % pisano_period
     
    previous, current = 0, 1
    if n==0:
        return 0
    elif n==1:
        return 1
    for i in range(n-1):
        previous, current \
        = current, previous + current
         
    return (current % m)


def lastDigitSum(n):
    a = 0
    b = 1
    sum = 1
    n = n % 60
    if n <= 1:
        return n
    else:
        for i in range(n-1):
            a , b = b, (a + b) % 60
            sum += b
            
    return sum % 10

def lastDigitPartialSum(m , n):
    m = m % 60
    n = n % 60
    a = 0
    b = 1
    sum = 0
    if m > n:
        n += 60 # to make sure n is bigger than m. 60一个循环，所以+60必然让n大于m
    for i in range(n + 1):
        if i >= m:
            sum += a

        a , b = b , (a + b) % 60
    return sum % 10

def lastDigitSquareSum(n):
    n = n % 60
    a = 0
    b = 1
    sum = 1
    if n <= 1:
        return n
    else:
        for i in range(n-1):
            c = a + b
            a = b
            b = c
            sum += b * b
        return sum % 10
def fiboNaive(n): 
    # compute then-th fibonacci number. 
    # Input: an integer n. 
    # Output: n-th fibonacci number
    if n <= 1:
        return n
    else:
        return fiboNaive(n-1) + fiboNaive(n-2)

def fiboEfficient(n):
    
    arr = [0,1]
    for i in range(2, n+1):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[n]




def lastDigitLarge(n):
    # Input: an integer n
    # Output: The last digit of n-th fibonacci number
    arr = [0,1]
    for i in range(2,n+1):
        arr.append((arr[i-1]+ arr[i-2]) % 10)
    
    return arr[n]

def pisano(m):
    a = 0
    b = 1
    c = a + b
    for i in range(m*m):
        c = (a + b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            return i+1

def fiboModulo(n,m):
    # F(n % period) % m == F(n) % m
    n = n % pisano(m)
    a = 0
    b = 1
    c = a + b
    if n <1:
        return n
    else:
        for i in range(n-1):
            c = (a + b) % m
            a = b
            b = c
        return c % m

def fiboModuloNaive(n, m):
    # input: Integer n and m
    # output: n-th fibonacci number modulo m
    a = 0
    b = 1
    if n <= 1:
        return n
    else: 
        for i in range(n-1):
            c = a+ b
            a = b
            b = c
        return b % m



if __name__ == '__main__':   

    #print(febRecursFast(int(input())))
    #a, b = map(int, input().split())
    #print(fibonacciModulo(a,b))
    #print(lastDigitSum(int(input())))
    #_from, _to = map(int , input().split())
    #print(lastDigitPartialSum(_from, _to))
    #print(lastDigitSum(int(inputNum)))
    #print(lastDigitLarge(inputNum))
    #m,n = map(int, input().split())
    print(lastDigitSquareSum(int(input())))