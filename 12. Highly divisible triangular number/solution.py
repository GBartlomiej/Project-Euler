from math import sqrt, ceil

def how_many_divisors(number : int):
    m = ceil(sqrt(number))
    count = 0
    for i in range(2,m):
        if number % i == 0:
            count += 1
    return (count*2)+2

for i in range(1,100000):
    triangle = int(i*(i+1)/2)
    if how_many_divisors(triangle)>500:
        break

print(int(i*(i+1)/2))
