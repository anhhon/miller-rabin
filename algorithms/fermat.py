import random
import time

# a^n mod p
def power(a, n, p):
     
    # Initialize result 
    res = 1
    # Update 'a' if 'a' >= p 
    a = a % p   
    while n > 0:
         
        # If n is odd, multiply 
        # 'a' with result 
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
             
            # n must be even now 
            n = n // 2
             
    return res % p

def isPrime(n, k):    
    # Corner cases
    if n<2: return False
    elif n == 2 or n == 3: return True

    # Try k times 
    else:
        for i in range(k):  
            # Pick a random number in [2..n-2]      
            # Above corner cases make sure that n > 4 
            a = random.randint(2, n - 1)
             
            # Fermat's little theorem 
            if power(a, n - 1, n) != 1:
                return False
                 
    return True


if __name__ == "__main__":
    # lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    start_time = time.perf_counter()

    # Pick n and choose k
    Test_Number = 15485863  
    repeatTime = 5

    # Execute Fermat
    if isPrime(Test_Number,repeatTime):
        print("Prime")
    else: print("Composite")

    # Compute calculation time
    end_time = time.perf_counter()
    exec_time = (end_time - start_time)*10**3
    print(f"Execution time: {exec_time:.3f}ms")
