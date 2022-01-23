def erasto(n):
    shouldBe = list(True for i in range(n+1))
    primes = list(range(n+1))
    m = 2
    while (m**2 <= n):
        if shouldBe[m]:
            for i in range(m * 2, n + 1, m):
                shouldBe[i] = False
        m += 1
    
    return [p for (p,b) in zip(primes,shouldBe) if b][2:]

def is_circular(prime, primes):
    string = str(prime)
    for i in string:
        string = string[-1]+string[:-1]
        if int(string) not in primes:
            return False
    return True

primes_under_million = set(erasto(1_000_000))
circular_primes= [prime for prime in primes_under_million if is_circular(prime, primes_under_million)]
print(circular_primes)
print(len(circular_primes))