import math
import array as arr
import time

def perfectPower(n):
    """Checks if number is a power of another integer, 
       if it returns true, then it is composite.
    """
    for b in range(2,int(math.log2(n))+1):       
        a=n**(1/b)
        if a-int(a) == 0:    
            return(True)    
    return(False)

def findR(n):
   """Find smallest r such that the order of n mod r > log2(n)^2.
   """
   maxK = math.log2(n)**2   
   maxR = math.log2(n)**5   
   nexR = True              
   r = 1                   
   while nexR == True:
       r +=1
       nexR = False
       k = 0
       while k <= maxK and nexR == False:
           k = k+1
           if fastMod(n,k,r) == 0 or fastMod(n,k,r) == 1:
               nexR = True
   return(r)

def fastMod(base,power,n):
    """Implement fast modular exponentiation.
    """
    r=1
    while power > 0:
        if power % 2 == 1:
            r = r * base % n
        base = base**2 % n
        power = power // 2
    return(r)

def fastPoly(base,power,r):
    """Use fast modular exponentiation for polynomials to raise them to a big power.
    """
    x = arr.array('d',[],)
    a = base[0]

    for i in range(len(base)):
        x.append(0)
    x[(0)] = 1 
    n = power
    
    while power > 0:
        if power % 2 == 1: 
            x = multi(x,base,n,r)
        base = multi(base,base,n,r)
        power = power // 2

    x[(0)] = x[(0)] - a
    x[(n % r )] = x[(n % r )] - 1        
    return(x)

def multi(a,b,n,r):
    """Function used by fastPoly to multiply two polynomials together.
    """ 
    x = arr.array('d',[])
    for i in range(len(a)+len(b)-1):
        x.append(0)
    for i in range(len(a)):
        for j in range(len(b)):
            x[(i+j) % r ] += a[(i)] * b[(j)] 
            x[(i+j) % r] = x[(i+j) % r] % n 
    for i in range(r,len(x)):
            x=x[:-1]
    return(x)

def eulerPhi(r):
    """Implement the euler phi function
    """
    x = 0        
    for i in range(1, r + 1):
        if math.gcd(r, i) == 1:
            x += 1
    return x


def aks(n):
    """ The main AKS algorithm
    """
    if perfectPower(n) == True:                     #step 1
        return('Composite')
    
    r = findR(n)                                    #step 2

    for a in range(2,min(r,n)):                     #step 3
        if math.gcd(a,n) > 1:                       
            return('Composite')

    if n <= r:                                      #step 4
        return('Prime')

    x = arr.array('l',[],)                         #step 5
    for a in range(1,math.floor((eulerPhi(r))**(1/2)*math.log2(n))):      
        x = fastPoly(arr.array('l',[a,1]),n,r)
        if  any(x):
            return('Composite')
    return('Prime')                                 #step 6


if __name__ == "__main__":
    # lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    start_time = time.perf_counter()

    # Pick n
    Test_Number = 15485863

    # Execute Fermat
    print(aks(Test_Number))
    # [print(aks(i)) for i in lowPrimes]

    # Compute calculation time
    end_time = time.perf_counter()
    exec_time = (end_time - start_time)*10**3
    print(f"Execution time: {exec_time:.3f}ms")