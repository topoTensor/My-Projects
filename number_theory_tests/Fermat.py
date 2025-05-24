primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43]

# EVERYTHING HERE IS EXPERIMENTAL AND JUST PROTOTYPING. 
# I wouldn't make the actual algorithms like this for real applications
def gcd(a,b):
    for q in range(2,a):
        if a%q==0 and b%q==0:
            return q
        
    return 1

def C(n,k):
    q=1
    for i in range(n-k+1, n+1):
        q*=i
    for i in range(1,k+1):
        q/=i
    return q
        
def Fermat_little_algorithm(a,p):
    accum=0
    for k in range(0,p-1):  
        print(k,"C: " , C(p-1,k)%(p))
        accum+=(((-1)**k)*(a**k)*((p-a)**(p-k-1)))*C(p-1,k)
        print(((-1)**k)*(a**k)*((p-a)**(p-k-1)), ((-1)**k)*(a**k)*((p-a)**(p-k-1))%p)
    print(accum, accum%p)
    
Fermat_little_algorithm(3,11)

def test():
    for p in primes:
        for a in range(1,p):
            for k in range(1,p):
                print(a**(p-1)%p, ((-1)**k * a ** k * (p-a)**(p-k-1))%p)
        
# test()

def factorial_mod(a,m):
    accum=1
    for i in range(1,a+1):
        accum *= i%m
    return accum%m

def Wilson(p):
    f=factorial_mod(p-1, p)
    return f==p-1

for i in range(2,100):
    if factorial_mod(i-1,i) != 0:
        print(i)