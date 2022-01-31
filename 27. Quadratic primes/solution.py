from sympy import ntheory

def how_many_primes(a, b):
    n = 0
    i = 0
    while True:
        number = n**2 + a*n + b
        if ntheory.primetest.isprime(number):
            i+=1
        else:
            return i
        n+=1

max = 0
for a in range(-1000,1000):
    for b in range(-1000,1001):
        how_many = how_many_primes(a,b)
        if how_many>max:
            max=how_many
            print(f"{how_many=}")
            print(f"Product: {a*b}")
            print("**************")




