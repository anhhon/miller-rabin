import random

# a^k mod n
def modPower(a,k,n):
    a = a % n
    res = 1 
    while(k>0):
        if(k&1):
            res = res * a % n
        a = a * a % n
        k >>= 1
    return res

# n-1 = 2^s.d -> (s,d)
def Decompose(n):
    s = 0
    d = n - 1
    while (d % 2 == 0):
        d = int(d/2)
        s += 1
    return (s,d)


def Witness(a, n):
    s,d = Decompose(n)
    x = modPower(a,d,n)                 # print("s,d,a,x=",s,d,a,x)

    for i in range(1,s+1):
        # Compute y ~ x^2 (mod n)
        y = x * x % n                   # print("loop i:",i,"-> y,x=",y,x)
        if y == 1 and x not in [1,n-1]:
            return False
        x = y
    
    if x != 1: return False
    return True


def MillerRabin(n, k):
    # Check n is small prime
    if n == 2 or n == 3 or n == 5 or n == 7: 
        return True
    if n < 11: 
        return False

    # Check n is even
    if n % 2 == 0: return False
    
    # Repeat Witness() with a random base 
    for i in range(k):
        # Pick a random number in [2..n-2] 
        a = random.randint(2, n - 2)
        if not Witness(a,n):
            return False
        
    return True


if __name__ == "__main__":

    # Pick n and choose k
    Test_Number = 561
    repeatTime = 2 

    if MillerRabin(Test_Number,repeatTime): 
        print("Prime")
    else: print("Composite")
